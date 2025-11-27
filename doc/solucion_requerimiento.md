# Solicitud de Información de XM

**Horizonte temporal ideal:** Últimos 24–36 meses

## Información Primaria (Obligatoria)

| Concepto                       | Detalle / Archivo Ejemplo                                                                                                  |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Precio de bolsa horario**    | Pool price / costo marginal (p. ej., `dMARmmdd.txt`)                                                                       |
| **Energía programada**         | Por recurso, 24 columnas horarias (p. ej., `dDECmmdd.txt`)                                                                 |
| **Participación en AGC**       | Por recurso (horario) (p. ej., `dAGCmmdd.txt`, `dAGCGenUnimmdd.txt`) y liquidaciones de AGC (SIC por agente/planta/unidad) |
| **Remuneración por capacidad** | Para unidades con OEF/ENFICC (RRID diario por planta/agente)                                                               |
| **Valores ex post reales**     | Para conciliación (true-up) (SIO: operación/generación diaria por recurso)                                                 |
| **Maestro de recursos**        | Diccionario de datos (IDs/nombres, último “Estándar de información del despacho”)                                          |

## Información Secundaria (Deseable / Complementario)

*   **Restricciones o ajustes de redespacho:** Por congestión, por agente/recurso.
*   **Salidas de servicio / disponibilidad:** Indisponibilidades para contexto.
*   **Compensación por arranque/parada:** O fuera de mérito aplicable al almacenamiento.
*   **Contratos bilaterales / PPP:** Estadísticas (público / agregado), o los mejores proxies disponibles.

---

# Análisis de Viabilidad: Requerimiento XM vs Datasets SIMEM

## Información Primaria (Obligatoria)

| Concepto Requerido                          | Dataset SIMEM Identificado                             | ID Dataset | Viabilidad | Observaciones                                   |
| :------------------------------------------ | :----------------------------------------------------- | :--------- | :--------- | :---------------------------------------------- |
| **Precio de bolsa horario**                 | Precio de bolsa horario                                | EC6945     | ✅ **ALTA** | Dataset directo disponible con precios horarios |
| **Energía programada por recurso**          | Generación programada en el despacho                   | E055B4     | ✅ **ALTA** | Datos horarios por recurso/planta               |
|                                             | Generación programada en el redespacho                 | 18F0B8     | ✅ **ALTA** | Complemento para redespacho                     |
|                                             | Despacho programado recursos de generación             | ff027b     | ✅ **ALTA** | Alternativa adicional                           |
| **Participación en AGC**                    | Reserva asignada como Control Automático de Generación | ea1c85     | ✅ **ALTA** | Datos horarios de AGC                           |
|                                             | Responsabilidad comercial de AGC                       | 520A3F     | ✅ **ALTA** | Liquidaciones de AGC                            |
|                                             | Costo unitario responsabilidad comercial de AGC        | 7BC5F5     | ✅ **ALTA** | Para valorización                               |
| **Remuneración por capacidad (OEF/ENFICC)** | Asignaciones de OEF por planta                         | 306c67     | ✅ **ALTA** | Asignaciones OEF                                |
|                                             | Valores del Cargo por Confiabilidad                    | 135c10     | ✅ **ALTA** | Valores de remuneración                         |
|                                             | Energía Firme del Cargo por Confiabilidad              | b38efc     | ✅ **ALTA** | Energía firme verificada                        |
|                                             | Obligación de energía firme por submercado             | BE51B1     | ✅ **ALTA** | Obligaciones OEF                                |
| **Valores ex post reales (SIO)**            | Generación Real y Programada en las Plantas            | E17D25     | ✅ **ALTA** | Generación real diaria                          |
|                                             | Generación real                                        | 055A4D     | ✅ **ALTA** | Valores reales operación                        |
|                                             | Disponibilidad real                                    | 9E77E5     | ✅ **ALTA** | Para conciliación                               |
| **Maestro de recursos**                     | Listado de plantas de generación                       | 7F18B1     | ✅ **ALTA** | Diccionario de plantas                          |
|                                             | Listado de unidades de generación                      | 670221     | ✅ **ALTA** | Detalle por unidad                              |
|                                             | Parámetros técnicos de plantas de generación           | 0bfc9d     | ✅ **ALTA** | Características técnicas                        |

## Información Secundaria (Deseable)

| Concepto Requerido                     | Dataset SIMEM Identificado                     | ID Dataset | Viabilidad  | Observaciones              |
| :------------------------------------- | :--------------------------------------------- | :--------- | :---------- | :------------------------- |
| **Restricciones/redespacho**           | Costo Marginal Redespacho                      | 03e35f     | ✅ **ALTA**  | Costos de redespacho       |
|                                        | Generación Programada Redespacho por Planta    | 12c7fd     | ✅ **ALTA**  | Redespacho por planta      |
|                                        | Restricciones a cargo de la demanda            | 00C31F     | 🟡 **MEDIA** | Restricciones generales    |
|                                        | Costo Restricciones Asignadas al Agente        | cf0167     | ✅ **ALTA**  | Por agente                 |
| **Salidas de servicio/disponibilidad** | Disponibilidad Real de las Unidades            | 64eb3f     | ✅ **ALTA**  | Disponibilidad del sistema |
|                                        | Histórico de eventos en Unidades de Generación | F28855     | ✅ **ALTA**  | Eventos históricos         |
|                                        | Eventos en unidades de Generación              | 7a07ac     | ✅ **ALTA**  | Eventos actuales           |
|                                        | Bandera de Disponibilidad Real                 | F3A9B1     | ✅ **ALTA**  | Indicadores disponibilidad |
| **Compensación arranque/parada**       | Precio de oferta arranque y parada             | e427a2     | ✅ **ALTA**  | Precios USD                |
|                                        | Precio de Oferta de Arranque y Parada          | 909809     | ✅ **ALTA**  | Por recurso USD            |
|                                        | Bandera de arranque Planta térmica             | 379022     | ✅ **ALTA**  | Indicadores arranque       |
|                                        | Bandera de arranque de plantas                 | 1237df     | ✅ **ALTA**  | Estado arranques           |
| **Contratos bilaterales/PPP**          | Datos soporte de Contratos por Recurso         | fa4671     | 🟡 **MEDIA** | Datos agregados            |
|                                        | Datos soporte de Contratos por versión horaria | ab3d66     | 🟡 **MEDIA** | Información limitada       |
|                                        | Estadísticas contratos mercado secundario      | 8DECCA     | 🟡 **MEDIA** | Solo estadísticas          |

## Resumen de Viabilidad

| Categoría                  | Viabilidad       | Cobertura |
| :------------------------- | :--------------- | :-------- |
| **Información Primaria**   | ✅ **MUY ALTA**   | ~95-100%  |
| **Información Secundaria** | 🟡 **ALTA-MEDIA** | ~70-80%   |

## Notas Importantes

### ✅ Puntos Fuertes
- **Precio de bolsa**: Disponible directamente (EC6945)
- **Generación programada y real**: Múltiples datasets complementarios
- **AGC**: Cobertura completa de participación y liquidaciones
- **Cargo por Confiabilidad**: Información detallada de OEF/ENFICC
- **Disponibilidad**: Eventos y estados bien documentados

### 🟡 Limitaciones
- **Contratos bilaterales**: Solo información agregada/estadística disponible públicamente
- **Detalles confidenciales**: Algunos datos específicos por agente pueden estar restringidos
- **Formato**: Puede requerir consolidación de múltiples datasets

### 📋 Recomendaciones

1. **Horizonte 24-36 meses**: Verificar disponibilidad histórica en cada dataset
2. **Acceso API**: Usar la API de datos abiertos de XM (https://www.simem.co)
3. **Consolidación**: Planificar proceso ETL para unificar múltiples fuentes
4. **Validación cruzada**: Usar datasets complementarios para verificar consistencia

## Estrategia de Obtención

### Fase 1: Datos Críticos (Alta Prioridad)
- EC6945, E055B4, ea1c85, 306c67, E17D25, 670221

### Fase 2: Datos Complementarios
- 18F0B8, 520A3F, 135c10, 055A4D, 0bfc9d

### Fase 3: Datos Contextuales
- 03e35f, 64eb3f, F28855, e427a2

---

**Conclusión**: El requerimiento es **altamente factible** (~85-90%) con los datasets públicos de SIMEM. La información primaria está prácticamente completa, mientras que algunos datos secundarios (especialmente contratos bilaterales detallados) pueden estar agregados o limitados por confidencialidad.