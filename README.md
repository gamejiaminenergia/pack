# SIMEM Data Extractor

Sistema automatizado para la extracción y consolidación de datos del Sistema de Intercambios Comerciales (SIMEM) de XM, diseñado para satisfacer los requerimientos de información del mercado eléctrico colombiano.

## 📋 Descripción del Proyecto

Este proyecto implementa una solución completa para obtener datos históricos del mercado eléctrico colombiano a través de la API pública de SIMEM. La solución aborda el **requerimiento de información de XM** con un horizonte temporal de 24-36 meses, cubriendo tanto información primaria (obligatoria) como secundaria (deseable).

### Solución al Requerimiento XM

El proyecto resuelve el requerimiento mediante la extracción automatizada de **32 datasets** de SIMEM que cubren:

#### ✅ Información Primaria (Cobertura: ~95-100%)

| Concepto Requerido             | Datasets Utilizados            | Viabilidad |
| :----------------------------- | :----------------------------- | :--------- |
| **Precio de bolsa horario**    | EC6945                         | ✅ ALTA     |
| **Energía programada**         | E055B4, 18F0B8, ff027b         | ✅ ALTA     |
| **Participación en AGC**       | ea1c85, 520A3F, 7BC5F5         | ✅ ALTA     |
| **Remuneración por capacidad** | 306c67, 135c10, b38efc, BE51B1 | ✅ ALTA     |
| **Valores ex post reales**     | E17D25, 055A4D, 9E77E5         | ✅ ALTA     |
| **Maestro de recursos**        | 7F18B1, 670221, 0bfc9d         | ✅ ALTA     |

#### 🟡 Información Secundaria (Cobertura: ~70-80%)

- **Restricciones/redespacho**: 03e35f, 12c7fd, 00C31F, cf0167
- **Disponibilidad**: 64eb3f, F28855, 7a07ac, F3A9B1
- **Compensación arranque/parada**: e427a2, 909809, 379022, 1237df
- **Contratos bilaterales**: fa4671, ab3d66, 8DECCA (datos agregados)

Ver [doc/solucion_requerimiento.md](doc/solucion_requerimiento.md) para el análisis detallado de viabilidad.

## 🚀 Características

- **Extracción asíncrona**: Descarga paralela de datos con control de concurrencia
- **Persistencia incremental**: Guarda datos inmediatamente para evitar pérdida en interrupciones
- **Validación automática**: Verifica integridad de archivos JSON descargados
- **Consolidación**: Genera archivos CSV consolidados por dataset
- **Documentación automática**: Extrae metadata y estructura de columnas de cada dataset
- **Diccionario de datos**: Genera documentación completa en formato Markdown
- **Configuración flexible**: Rango de fechas y datasets configurables
- **Logging completo**: Registro detallado de operaciones y errores

## 📁 Estructura del Proyecto

```
pack/
├── config.py                    # Configuración (fechas, datasets)
├── dataset_ids.json            # IDs de datasets SIMEM
├── simem_synchronization.py    # Extractor asíncrono principal
├── simem_documentacion.py      # Extractor de metadata y columnas
├── crear_diccionario.py        # Generador de diccionario Markdown
├── simem_check.py              # Validador de archivos JSON
├── read_data.py                # Consolidador de datos a CSV
├── diccionario.md              # Diccionario de datos generado
├── requirements.txt            # Dependencias Python
├── data/
│   ├── simem/
│   │   └── {dataset_id}/       # Datos JSON por dataset y fecha
│   │       └── YYYY-MM-DD.json
│   └── simem_documentation/    # Metadata y columnas por dataset
│       └── {dataset_id}.json
├── tmp/
│   └── {dataset_id}.csv        # Archivos CSV consolidados
└── doc/
    └── solucion_requerimiento.md  # Análisis de viabilidad
```

## 🔧 Instalación

### Requisitos

- Python 3.12+
- Entorno virtual (recomendado)

### Pasos

1. **Clonar el repositorio**
   ```bash
   cd pack
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Uso

### 1. Configurar Parámetros

Editar `config.py` para definir el rango de fechas:

```python
@dataclass
class Config:
    date_min: datetime.date = field(default_factory=lambda: datetime.date(2025, 10, 1))
    date_max: datetime.date = field(default_factory=lambda: datetime.date(2025, 10, 31))
    dataset_ids: List = field(default_factory=load_dataset_ids)
```

### 2. Extraer Datos de SIMEM

```bash
python simem_synchronization.py
```

**Características:**
- Descarga datos de la API pública de SIMEM
- Guarda archivos JSON en `data/simem/{dataset_id}/{fecha}.json`
- Omite archivos ya descargados (reanudable)
- Muestra progreso en tiempo real

**Ejemplo de salida:**
```
📊 Iniciando extracción asíncrona...
   Fechas: 31
   Datasets: 32
   Total posible: 992
   Ya existentes: 0
   Por descargar: 992
   Conexiones simultáneas: 5
Descargando: 100%|████████| 992/992 [05:30<00:00, 3.00request/s]
✅ Extracción completada!
   Descargados exitosamente: 900/992
   Fallidos: 92
```

### 3. Validar Integridad de Datos

```bash
python simem_check.py
```

Verifica que todos los archivos JSON sean válidos y elimina los corruptos.

### 4. Consolidar Datos a CSV

```bash
python read_data.py
```

Genera archivos CSV consolidados en `tmp/{dataset_id}.csv` combinando todos los archivos JSON de cada dataset.

### 5. Extraer Documentación de Datasets

```bash
python simem_documentacion.py
```

**Características:**
- Extrae `metadata` y `columns` de cada dataset desde la API de SIMEM
- Busca la primera metadata no vacía en el rango de fechas configurado
- Guarda documentación en `data/simem_documentation/{dataset_id}.json`
- Omite datasets ya documentados (reanudable)
- Muestra progreso en tiempo real

**Ejemplo de salida:**
```
📊 Iniciando extracción de documentación...
   Datasets a procesar: 32
   Rango de fechas: 2025-10-01 a 2025-10-31
   Conexiones simultáneas: 5
Procesando datasets: 100%|████████| 32/32 [01:54<00:00, 3.57s/dataset]
✅ Extracción de documentación completada!
```

**Estructura del JSON generado:**
```json
{
  "metadata": {
    "description": "Descripción del dataset",
    "entity": "XM",
    "category": "Categoría del dataset",
    "periodicity": "Diaria",
    "granularity": "Horaria",
    "creationDate": "2023-09-28 22:45:20",
    "lastUpdate": "2025-11-27 10:31:45",
    "nextUpdateDate": "2025-11-28 10:00:00",
    "historicData": "URL de datos históricos",
    "ultimaNovedad": {
      "titulo": "Título de la novedad",
      "descripcion": "Descripción",
      "fechaPublicacion": "2024-03-12",
      "urlNovedad": "URL"
    }
  },
  "columns": [
    {
      "nameColumn": "NombreColumna",
      "dataType": "tipo",
      "description": "Descripción de la columna"
    }
  ],
  "date": "2025-10-01"
}
```

### 6. Generar Diccionario de Datos

```bash
python crear_diccionario.py
```

**Características:**
- Genera un diccionario completo en formato Markdown (`diccionario.md`)
- Incluye índice navegable con links internos
- Documenta metadata, columnas y novedades de cada dataset
- Formato profesional con tablas y emojis

**Contenido del diccionario:**
- 📚 Encabezado con total de datasets y fecha de generación
- 📑 Índice navegable con categorías
- 📊 Información general de cada dataset
- 📢 Últimas novedades (cuando existen)
- 📋 Tablas de columnas con tipos y descripciones

**Ejemplo de salida:**
```
🚀 Iniciando generación del diccionario...
📊 Total de datasets cargados: 32
📝 Generando contenido Markdown...
✅ Diccionario creado exitosamente: diccionario.md
📄 Tamaño del archivo: 43695 caracteres
🏁 Proceso completado!
```

## 🔑 Datasets Incluidos

El proyecto extrae **32 datasets** identificados en el análisis de viabilidad:

<details>
<summary><b>Ver lista completa de datasets</b></summary>

| ID Dataset | Descripción                                     |
| :--------- | :---------------------------------------------- |
| EC6945     | Precio de bolsa horario                         |
| E055B4     | Generación programada en el despacho            |
| 18F0B8     | Generación programada en el redespacho          |
| ff027b     | Despacho programado recursos de generación      |
| ea1c85     | Reserva asignada como AGC                       |
| 520A3F     | Responsabilidad comercial de AGC                |
| 7BC5F5     | Costo unitario responsabilidad comercial de AGC |
| 306c67     | Asignaciones de OEF por planta                  |
| 135c10     | Valores del Cargo por Confiabilidad             |
| b38efc     | Energía Firme del Cargo por Confiabilidad       |
| BE51B1     | Obligación de energía firme por submercado      |
| E17D25     | Generación Real y Programada en las Plantas     |
| 055A4D     | Generación real                                 |
| 9E77E5     | Disponibilidad real                             |
| 7F18B1     | Listado de plantas de generación                |
| 670221     | Listado de unidades de generación               |
| 0bfc9d     | Parámetros técnicos de plantas de generación    |
| 03e35f     | Costo Marginal Redespacho                       |
| 12c7fd     | Generación Programada Redespacho por Planta     |
| 00C31F     | Restricciones a cargo de la demanda             |
| cf0167     | Costo Restricciones Asignadas al Agente         |
| 64eb3f     | Disponibilidad Real de las Unidades             |
| F28855     | Histórico de eventos en Unidades de Generación  |
| 7a07ac     | Eventos en unidades de Generación               |
| F3A9B1     | Bandera de Disponibilidad Real                  |
| e427a2     | Precio de oferta arranque y parada              |
| 909809     | Precio de Oferta de Arranque y Parada           |
| 379022     | Bandera de arranque Planta térmica              |
| 1237df     | Bandera de arranque de plantas                  |
| fa4671     | Datos soporte de Contratos por Recurso          |
| ab3d66     | Datos soporte de Contratos por versión horaria  |
| 8DECCA     | Estadísticas contratos mercado secundario       |

</details>

## 📊 Formato de Datos

### Archivos JSON (raw)
```json
[
  {
    "Id": "123456",
    "Values_code": "EC6945",
    "Date": "2025-10-01T00:00:00",
    "Hour": 1,
    "Value": 245.67
  }
]
```

### Archivos CSV (consolidados)
Cada CSV contiene todos los registros del dataset para el rango de fechas configurado.

## 🛠️ Tecnologías

- **Python 3.12**: Lenguaje principal
- **aiohttp**: Cliente HTTP asíncrono para API
- **pandas**: Procesamiento y consolidación de datos
- **tqdm**: Barras de progreso
- **asyncio**: Programación asíncrona

## 📝 Logs

- `simem_sync.log`: Log de sincronización de datos
- `simem_doc.log`: Log de extracción de documentación
- `db_sync.log`: Log de consolidación a CSV

## ⚙️ Configuración Avanzada

### Modificar concurrencia

En `simem_synchronization.py`:
```python
extractor = SimemExtractorAsync(max_concurrent=5)  # Ajustar según necesidad
```

### Agregar/quitar datasets

Editar `dataset_ids.json`:
```json
[
  "EC6945",
  "E055B4",
  ...
]
```

## 🔍 Solución de Problemas

### Error: ModuleNotFoundError
```bash
# Asegurarse de usar el entorno virtual
source venv/bin/activate
pip install -r requirements.txt
```

### Archivos corruptos
```bash
# Ejecutar validador para limpiar
python simem_check.py
```

### Reintentar descargas fallidas
```bash
# Simplemente volver a ejecutar, omitirá archivos existentes
python simem_synchronization.py
```

## 🔄 Flujo de Trabajo Recomendado

Para obtener datos completos y documentación, seguir este orden:

```bash
# 1. Extraer datos históricos (records)
python simem_synchronization.py

# 2. Validar integridad de los datos
python simem_check.py

# 3. Consolidar datos a CSV
python read_data.py

# 4. Extraer documentación (metadata y columnas)
python simem_documentacion.py

# 5. Generar diccionario de datos
python crear_diccionario.py
```

**Resultado final:**
- ✅ Datos históricos en `data/simem/{dataset_id}/`
- ✅ CSVs consolidados en `tmp/`
- ✅ Documentación técnica en `data/simem_documentation/`
- ✅ Diccionario completo en `diccionario.md`

## 📄 Licencia

Este proyecto es de código abierto para uso académico y de investigación.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Contacto

Para preguntas sobre el requerimiento XM o el análisis de viabilidad, consultar [doc/solucion_requerimiento.md](doc/solucion_requerimiento.md).

---

**Nota**: Este proyecto utiliza la API pública de SIMEM (https://www.simem.co). Respetar los términos de uso y límites de tasa de la API.
