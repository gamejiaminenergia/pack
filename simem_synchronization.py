import logging
import os
from config import config
import aiohttp
import asyncio
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any
from tqdm.asyncio import tqdm as async_tqdm

# Configuración de logging
log_file = 'simem_sync.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()  # También mostrar en consola
    ]
)
logger = logging.getLogger(__name__)

class SimemExtractorAsync:
    def __init__(self, base_url: str = "https://www.simem.co/backend-files/api/PublicData", max_concurrent: int = 5):
        self.base_url = base_url
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
    async def get_data(self, session: aiohttp.ClientSession, date: str, dataset_id: str) -> tuple[str, str, Dict[str, Any]]:
        """
        Obtiene datos de la API de forma asíncrona
        """
        logger.debug(f"🔄 Solicitando datos: {date} | {dataset_id}")
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
                    
                    if data.get('success'):
                        records_count = len(data.get('result', {}).get('records', []))
                        logger.info(f"✅ {date} | {dataset_id} | {records_count} records")
                    else:
                        logger.warning(f"⚠️ Respuesta no exitosa: {date} | {dataset_id}")
                    
                    return date, dataset_id, data
                    
            except asyncio.TimeoutError:
                logger.warning(f"⌛ Timeout: {date} | {dataset_id}")
                return date, dataset_id, None
            except aiohttp.ClientError as e:
                logger.error(f"❌ Error conexión: {date} | {dataset_id} | {e}")
                return date, dataset_id, None
            except json.JSONDecodeError as e:
                logger.error(f"❌ Error JSON: {date} | {dataset_id} | {e}")
                return date, dataset_id, None
            except Exception as e:
                logger.error(f"❌ Error inesperado: {date} | {dataset_id} | {e}")
                return date, dataset_id, None
    
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
    
    def save_data(self, data: Dict[str, Any], dataset_id: str, date: str):
        """
        Guarda los records de la respuesta en un archivo JSON
        """
        if not data:
            return
            
        if 'result' not in data or 'records' not in data['result']:
            logger.warning(f"⚠️ Estructura incorrecta: {date} | {dataset_id}")
            return
            
        records = data['result']['records']
        if not records:
            logger.warning(f"⚠️ Sin records: {date} | {dataset_id}")
            return
            
        directory = Path(f"data/simem/{dataset_id}")
        directory.mkdir(parents=True, exist_ok=True)
        
        filepath = directory / f"{date}.json"
        
        if filepath.exists():
            return
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(records, f, indent=2, ensure_ascii=False)
    
    async def extract_data_range(self,
                                start_date: datetime,
                                end_date: datetime,
                                dataset_ids: List[str]):
        """
        Extrae datos de forma asíncrona con límite de conexiones concurrentes
        """
        dates = self.generate_date_range(start_date, end_date)
        
        # Filtrar tareas que no necesitan ejecutarse
        tasks_to_run = []
        for dataset_id in dataset_ids:
            for date in dates:
                filepath = Path(f"data/simem/{dataset_id}/{date}.json")
                if not filepath.exists():
                    tasks_to_run.append((date, dataset_id))
        
        total_tasks = len(tasks_to_run)
        total_skipped = len(dates) * len(dataset_ids) - total_tasks
        
        logger.info(f"📊 Iniciando extracción asíncrona...")
        logger.info(f"   Fechas: {len(dates)}")
        logger.info(f"   Datasets: {len(dataset_ids)}")
        logger.info(f"   Total posible: {len(dates) * len(dataset_ids)}")
        logger.info(f"   Ya existentes: {total_skipped}")
        logger.info(f"   Por descargar: {total_tasks}")
        logger.info(f"   Conexiones simultáneas: {self.max_concurrent}")
        logger.info("-" * 60)
        
        if total_tasks == 0:
            logger.info("✅ Todos los archivos ya existen. No hay nada que descargar.")
            return
        
        # Crear sesión HTTP única para todas las peticiones
        connector = aiohttp.TCPConnector(limit=self.max_concurrent)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            # Crear todas las tareas
            tasks = [
                self.get_data(session, date, dataset_id)
                for date, dataset_id in tasks_to_run
            ]
            
            # Ejecutar con barra de progreso
            results = []
            saved_count = 0
            for coro in async_tqdm(
                asyncio.as_completed(tasks),
                total=len(tasks),
                desc='Descargando',
                unit='request',
                colour='green'
            ):
                date, dataset_id, data = await coro
                if data:
                    self.save_data(data, dataset_id, date)
                    saved_count += 1
        
        logger.info(f"\n✅ Extracción completada!")
        logger.info(f"   Descargados exitosamente: {saved_count}/{total_tasks}")
        logger.info(f"   Fallidos: {total_tasks - saved_count}")

async def main():
    logger.info("🚀 Iniciando sincronización SIMEM")
    extractor = SimemExtractorAsync(max_concurrent=5)
    
    await extractor.extract_data_range(
        start_date=config.date_min,
        end_date=config.date_max,
        dataset_ids=config.dataset_ids
    )
    logger.info("🏁 Sincronización SIMEM completada")

if __name__ == "__main__":

    # print(config.date_min)
    # print(config.date_max)
    # print(config.dataset_ids)

    asyncio.run(main())