import logging
import os
from config import config
import aiohttp
import asyncio
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional
from tqdm.asyncio import tqdm as async_tqdm

# Configuración de logging
log_file = 'simem_doc.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()  # También mostrar en consola
    ]
)
logger = logging.getLogger(__name__)

class SimemDocumentationExtractor:
    def __init__(self, base_url: str = "https://www.simem.co/backend-files/api/PublicData", max_concurrent: int = 5):
        self.base_url = base_url
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
    async def get_metadata_and_columns(self, session: aiohttp.ClientSession, date: str, dataset_id: str) -> tuple[str, Optional[Dict[str, Any]]]:
        """
        Obtiene metadata y columns de la API de forma asíncrona
        """
        logger.debug(f"🔄 Solicitando metadata: {date} | {dataset_id}")
        params = {
            'startDate': date,
            'endDate': date,
            'datasetId': dataset_id
        }
        
        async with self.semaphore:  # Limita conexiones concurrentes
            try:
                async with session.get(self.base_url, params=params, timeout=30) as response:
                    response.raise_for_status()
                    data = await response.json()
                    
                    if data.get('success') and 'result' in data:
                        result = data['result']
                        metadata = result.get('metadata', {})
                        columns = result.get('columns', [])
                        
                        # Verificar si hay metadata o columns no vacíos
                        if metadata or columns:
                            logger.info(f"✅ {date} | {dataset_id} | Metadata encontrada")
                            return dataset_id, {
                                'metadata': metadata,
                                'columns': columns,
                                'date': date
                            }
                        else:
                            logger.debug(f"⚠️ Metadata vacía: {date} | {dataset_id}")
                            return dataset_id, None
                    else:
                        logger.warning(f"⚠️ Respuesta no exitosa: {date} | {dataset_id}")
                        return dataset_id, None
                        
            except asyncio.TimeoutError:
                logger.warning(f"⌛ Timeout: {date} | {dataset_id}")
                return dataset_id, None
            except aiohttp.ClientError as e:
                logger.error(f"❌ Error conexión: {date} | {dataset_id} | {e}")
                return dataset_id, None
            except json.JSONDecodeError as e:
                logger.error(f"❌ Error JSON: {date} | {dataset_id} | {e}")
                return dataset_id, None
            except Exception as e:
                logger.error(f"❌ Error inesperado: {date} | {dataset_id} | {e}")
                return dataset_id, None
    
    def generate_date_range(self, start_date: datetime, end_date: datetime) -> List[str]:
        """
        Genera un rango de fechas diarias
        """
        dates = []
        current = start_date
        while current <= end_date:
            dates.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=1)
        return dates
    
    def save_documentation(self, dataset_id: str, doc_data: Dict[str, Any]):
        """
        Guarda la metadata y columns en un archivo JSON
        """
        directory = Path("data/simem_documentation")
        directory.mkdir(parents=True, exist_ok=True)
        
        filepath = directory / f"{dataset_id}.json"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(doc_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Documentación guardada: {dataset_id}")
    
    async def extract_documentation(self,
                                   start_date: datetime,
                                   end_date: datetime,
                                   dataset_ids: List[str]):
        """
        Extrae metadata y columns para cada dataset
        Para cada dataset, busca la primera metadata/columns no vacía
        """
        dates = self.generate_date_range(start_date, end_date)
        
        # Verificar qué datasets ya tienen documentación
        datasets_to_process = []
        for dataset_id in dataset_ids:
            filepath = Path(f"data/simem_documentation/{dataset_id}.json")
            if not filepath.exists():
                datasets_to_process.append(dataset_id)
            else:
                logger.info(f"⏭️ Ya existe documentación para: {dataset_id}")
        
        if not datasets_to_process:
            logger.info("✅ Todos los datasets ya tienen documentación.")
            return
        
        logger.info(f"📊 Iniciando extracción de documentación...")
        logger.info(f"   Datasets a procesar: {len(datasets_to_process)}")
        logger.info(f"   Rango de fechas: {dates[0]} a {dates[-1]}")
        logger.info(f"   Conexiones simultáneas: {self.max_concurrent}")
        logger.info("-" * 60)
        
        # Crear sesión HTTP única para todas las peticiones
        connector = aiohttp.TCPConnector(limit=self.max_concurrent)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            # Procesar cada dataset secuencialmente
            for dataset_id in async_tqdm(datasets_to_process, desc='Procesando datasets', unit='dataset', colour='blue'):
                logger.info(f"\n🔍 Buscando documentación para: {dataset_id}")
                
                # Buscar en cada fecha hasta encontrar metadata no vacía
                found = False
                for date in dates:
                    _, doc_data = await self.get_metadata_and_columns(session, date, dataset_id)
                    
                    if doc_data:
                        # Encontramos metadata/columns no vacía
                        self.save_documentation(dataset_id, doc_data)
                        found = True
                        break
                
                if not found:
                    logger.warning(f"⚠️ No se encontró metadata para {dataset_id} en el rango de fechas")
        
        logger.info(f"\n✅ Extracción de documentación completada!")

async def main():
    logger.info("🚀 Iniciando extracción de documentación SIMEM")
    extractor = SimemDocumentationExtractor(max_concurrent=5)
    
    await extractor.extract_documentation(
        start_date=config.date_min,
        end_date=config.date_max,
        dataset_ids=config.dataset_ids
    )
    logger.info("🏁 Extracción de documentación SIMEM completada")

if __name__ == "__main__":
    asyncio.run(main())
