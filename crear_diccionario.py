import json
import logging
from pathlib import Path
from typing import Dict, Any, List

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DiccionarioGenerator:
    def __init__(self, documentation_dir: str = "data/simem_documentation"):
        self.documentation_dir = Path(documentation_dir)
        self.output_file = "diccionario.md"
    
    def load_all_documentation(self) -> List[Dict[str, Any]]:
        """
        Carga todos los archivos JSON de documentación
        """
        all_docs = []
        
        if not self.documentation_dir.exists():
            logger.error(f"❌ El directorio {self.documentation_dir} no existe")
            return all_docs
        
        json_files = sorted(self.documentation_dir.glob("*.json"))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data['dataset_id'] = json_file.stem  # Agregar el ID del dataset
                    all_docs.append(data)
                    logger.info(f"✅ Cargado: {json_file.name}")
            except Exception as e:
                logger.error(f"❌ Error al cargar {json_file.name}: {e}")
        
        return all_docs
    
    def generate_markdown(self, docs: List[Dict[str, Any]]) -> str:
        """
        Genera el contenido del diccionario en formato Markdown
        """
        md_content = []
        
        # Encabezado principal
        md_content.append("# 📚 Diccionario de Datos SIMEM\n")
        md_content.append(f"**Total de Datasets:** {len(docs)}\n")
        md_content.append(f"**Fecha de generación:** {docs[0].get('date', 'N/A') if docs else 'N/A'}\n")
        md_content.append("---\n")
        
        # Tabla de contenidos
        md_content.append("## 📑 Índice de Datasets\n")
        for i, doc in enumerate(docs, 1):
            dataset_id = doc.get('dataset_id', 'Unknown')
            category = doc.get('metadata', {}).get('category', 'Sin categoría')
            md_content.append(f"{i}. [{dataset_id}](#{dataset_id.lower()}) - {category}\n")
        
        md_content.append("\n---\n\n")
        
        # Detalles de cada dataset
        for doc in docs:
            dataset_id = doc.get('dataset_id', 'Unknown')
            metadata = doc.get('metadata', {})
            columns = doc.get('columns', [])
            
            # Encabezado del dataset
            md_content.append(f"## {dataset_id}\n")
            
            # Metadata
            md_content.append("### 📊 Información General\n")
            md_content.append(f"**Descripción:** {metadata.get('description', 'N/A')}\n\n")
            md_content.append(f"- **Entidad:** {metadata.get('entity', 'N/A')}\n")
            md_content.append(f"- **Categoría:** {metadata.get('category', 'N/A')}\n")
            md_content.append(f"- **Periodicidad:** {metadata.get('periodicity', 'N/A')}\n")
            md_content.append(f"- **Granularidad:** {metadata.get('granularity', 'N/A')}\n")
            md_content.append(f"- **Fecha de creación:** {metadata.get('creationDate', 'N/A')}\n")
            md_content.append(f"- **Última actualización:** {metadata.get('lastUpdate', 'N/A')}\n")
            md_content.append(f"- **Próxima actualización:** {metadata.get('nextUpdateDate', 'N/A')}\n")
            
            if metadata.get('historicData'):
                md_content.append(f"- **Datos históricos:** [{metadata.get('historicData')}]({metadata.get('historicData')})\n")
            
            # Novedad si existe
            if metadata.get('ultimaNovedad'):
                novedad = metadata['ultimaNovedad']
                md_content.append("\n#### 📢 Última Novedad\n")
                md_content.append(f"**{novedad.get('titulo', '')}**\n\n")
                if novedad.get('subtitulo'):
                    md_content.append(f"*{novedad.get('subtitulo')}*\n\n")
                md_content.append(f"{novedad.get('descripcion', '')}\n\n")
                md_content.append(f"- **Fecha:** {novedad.get('fechaPublicacion', 'N/A')}\n")
                if novedad.get('urlNovedad'):
                    md_content.append(f"- **Más información:** [{novedad.get('urlNovedad')}]({novedad.get('urlNovedad')})\n")
            
            # Columnas
            md_content.append("\n### 📋 Estructura de Datos (Columnas)\n")
            
            if columns:
                md_content.append("| Columna | Tipo de Dato | Descripción |\n")
                md_content.append("|---------|--------------|-------------|\n")
                
                for col in columns:
                    name = col.get('nameColumn', 'N/A')
                    data_type = col.get('dataType', 'N/A')
                    description = col.get('description', 'N/A').replace('\n', ' ').strip()
                    md_content.append(f"| `{name}` | {data_type} | {description} |\n")
            else:
                md_content.append("*No hay información de columnas disponible.*\n")
            
            md_content.append("\n---\n\n")
        
        return ''.join(md_content)
    
    def create_dictionary(self):
        """
        Crea el archivo diccionario.md
        """
        logger.info("🚀 Iniciando generación del diccionario...")
        
        # Cargar documentación
        docs = self.load_all_documentation()
        
        if not docs:
            logger.error("❌ No se encontraron documentos para procesar")
            return
        
        logger.info(f"📊 Total de datasets cargados: {len(docs)}")
        
        # Generar contenido Markdown
        logger.info("📝 Generando contenido Markdown...")
        md_content = self.generate_markdown(docs)
        
        # Guardar archivo
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            logger.info(f"✅ Diccionario creado exitosamente: {self.output_file}")
            logger.info(f"📄 Tamaño del archivo: {len(md_content)} caracteres")
        except Exception as e:
            logger.error(f"❌ Error al guardar el archivo: {e}")

def main():
    generator = DiccionarioGenerator()
    generator.create_dictionary()
    print("\n🏁 Proceso completado!")

if __name__ == "__main__":
    main()
