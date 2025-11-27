# 📚 Diccionario de Datos SIMEM
**Total de Datasets:** 32
**Fecha de generación:** 2025-10-01
---
## 📑 Índice de Datasets
1. [00C31F](#00c31f) - Restricciones a cargo de la demanda
2. [03e35f](#03e35f) - Costo Marginal Redespacho
3. [055A4D](#055a4d) - Generación real
4. [0bfc9d](#0bfc9d) - Parámetros técnicos de las plantas de generación
5. [1237df](#1237df) - Bandera de arranque de plantas
6. [12c7fd](#12c7fd) - Generación Programada Redespacho por Planta
7. [135c10](#135c10) - Valores del Cargo por Confiabilidad
8. [18F0B8](#18f0b8) - Generación programada en el redespacho
9. [306c67](#306c67) - Asignaciones de OEF por planta
10. [379022](#379022) - Bandera de arranque Planta térmica para el Despacho Ideal
11. [520A3F](#520a3f) - Responsabilidad comercial de AGC
12. [64eb3f](#64eb3f) - Disponibilidad Real de las Unidades de Generación del Sistema
13. [670221](#670221) - Listado de unidades de generación
14. [7BC5F5](#7bc5f5) - Costo unitario responsabilidad comercial de AGC
15. [7F18B1](#7f18b1) - Listado de plantas de generación en pruebas
16. [7a07ac](#7a07ac) - Eventos en unidades de Generación
17. [8DECCA](#8decca) - Estadísticas de contratos del mercado secundario
18. [909809](#909809) - Precio de Oferta de Arranque y Parada por recurso USD
19. [9E77E5](#9e77e5) - Disponibilidad real
20. [BE51B1](#be51b1) - Obligación de energía firme por submercado
21. [E055B4](#e055b4) - Generación programada en el despacho
22. [E17D25](#e17d25) - Generación Real y Programada en las Plantas de Generación
23. [EC6945](#ec6945) - Precio de bolsa horario
24. [F28855](#f28855) - Histórico de eventos en Unidades de Generación
25. [F3A9B1](#f3a9b1) - Bandera de Disponibilidad Real
26. [ab3d66](#ab3d66) - Datos soporte del proceso de Contratos por versión y horaria
27. [b38efc](#b38efc) - Energía Firme del Cargo por Confiabilidad verificada por el Centro Nacional de Despacho
28. [cf0167](#cf0167) - Costo Restricciones Asignadas al Agente
29. [e427a2](#e427a2) - Precio oferta arranque y parada por unidad para el combustible USD
30. [ea1c85](#ea1c85) - Reserva asignada como Control Automático de Generación
31. [fa4671](#fa4671) - Datos soporte del proceso de Contratos por Recurso, versión y diaria
32. [ff027b](#ff027b) - Despacho programado recursos de generación

---

## 00C31F
### 📊 Información General
**Descripción:** Valor de las restricciones a cargo de la demanda asignadas al agente, en pesos COP.

- **Entidad:** XM
- **Categoría:** Restricciones a cargo de la demanda
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2024-11-07 10:33:56
- **Última actualización:** 2025-11-19 20:25:30
- **Próxima actualización:** 2025-11-20 11:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 03e35f
### 📊 Información General
**Descripción:** Contiene el costo marginal considerando el último redespacho para el día de operación publicado por el Centro Nacional de Despacho (CND) para el Sistema Interconectado Nacional (SIN)

- **Entidad:** XM
- **Categoría:** Costo Marginal Redespacho
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-30 21:53:06
- **Última actualización:** 2025-11-27 07:20:40
- **Próxima actualización:** 2025-11-28 07:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CostoMarginalRedespacho` | decimal | Costo marginal del redespacho |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 055A4D
### 📊 Información General
**Descripción:** Generación real de cada una de las plantas, en kWh.

- **Entidad:** XM
- **Categoría:** Generación real
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-28 22:45:20
- **Última actualización:** 2025-11-27 10:31:45
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 0bfc9d
### 📊 Información General
**Descripción:** Contiene la información de agente Operador, Capacidad efectiva neta, tecnología de generación, Fecha de Puesta en Operación Comercial (FPO) e información de retiro de las plantas hidraúlicas que se encuentran en operación comercial.

- **Entidad:** XM
- **Categoría:** Parámetros técnicos de las plantas de generación
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-02-07 14:10:00
- **Última actualización:** 2025-11-27 11:18:41
- **Próxima actualización:** 2025-11-28 11:00:00
- **Datos históricos:** [NA](NA)

#### 📢 Última Novedad
**Creación de conjunto unificado de Parámetros técnicos de las plantas de generación**

*Creación de conjunto unificado de Parámetros técnicos de las plantas de generación*

A partir de la fecha 2025-03-07, éste conjunto de datos reemplazará los 4 conjuntos individuales relacionados a Parámetros técnicos de las plantas de generación (Eólicas, Solares, Hidráulicas y Térmicas)

- **Fecha:** 2025-03-05
- **Más información:** [https://www.simem.co/pages/novedadesDetalle;id=76418F4B-CB7F-478E-0875-08DD5BEA5F75](https://www.simem.co/pages/novedadesDetalle;id=76418F4B-CB7F-478E-0875-08DD5BEA5F75)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `NombrePlanta` | texto | Nombre de la planta/recurso de generación |
| `CodigoPlanta` | texto | Código de la planta |
| `CodigoAreaOperativa` | texto | Código del área operativa eléctrica |
| `TipoGeneracion` | texto | Tipo de clasificación del recurso de generación |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `TipoClasificacion` | texto | Clasificación del generador según la regulación actual |
| `CodigoSubAreaOperativa` | texto | Código de la subárea asociada al activo |
| `CapEfectivaNeta` | decimal | Capacidad Efectiva Neta de las plantas de generación |
| `FPO` | fecha | Fecha de Puesta en Operación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |
| `Fecha` | fecha | Fecha de representación de la información |
| `TipoDespachoRecurso` | texto | Tipo de despacho del recurso |

---

## 1237df
### 📊 Información General
**Descripción:** Bandera de arranque de una planta de generación, este valor binario indica que cuando el dato sea igual a 1, la planta inicia operación

- **Entidad:** XM
- **Categoría:** Bandera de arranque de plantas
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-10-10 15:45:15
- **Última actualización:** 2025-10-16 02:39:59
- **Próxima actualización:** 2025-10-15 09:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `CodigoPlanta` | texto | Código de la planta |
| `ValorTexto` | texto | Valor de la variable indicada |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 12c7fd
### 📊 Información General
**Descripción:** Contiene la generación programada considerando el último redespacho para cada planta de generación publicado por el Centro Nacional de Despacho (CND)

- **Entidad:** XM
- **Categoría:** Generación Programada Redespacho por Planta
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-30 12:57:24
- **Última actualización:** 2025-11-27 07:21:49
- **Próxima actualización:** 2025-11-28 07:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `GeneracionProgramadaRedespacho` | decimal | Generación programada en el redespacho |
| `CodigoElementoGeneracion` | texto | Código del Elemento de Generación: Planta o Unidad |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 135c10
### 📊 Información General
**Descripción:** Valores del Cargo por Confiabilidad en USD/MWh que aplican para cada Período Cargo a cada planta que tenga asignaciones de Obligaciones de Energía firme (OEF) en dicho período. El precio se actualizará solo para las OEF vigentes a la fecha actual. 

- **Entidad:** XM
- **Categoría:** Valores del Cargo por Confiabilidad
- **Periodicidad:** Anual
- **Granularidad:** Anual
- **Fecha de creación:** 2023-09-28 21:19:03
- **Última actualización:** 2025-11-27 00:08:34
- **Próxima actualización:** 2025-12-06 08:00:00
- **Datos históricos:** [https://www.xm.com.co/transacciones/asignacion-subastas/subasta-de-energia-firme-2](https://www.xm.com.co/transacciones/asignacion-subastas/subasta-de-energia-firme-2)

#### 📢 Última Novedad
**Accede a los datos de la cuarta subasta para la asignación de OEF**

La cuarta subasta para la asignación de OEF para el periodo comprendido entre el 1° de diciembre de 2027 y el 30 de noviembre de 2028 ha concluido y ya puedes consultar los resultados.

- **Fecha:** 2024-03-12
- **Más información:** [https://www.simem.co/pages/novedadesDetalle;id=6299A6FB-0285-4583-A758-1D3C0B588734](https://www.simem.co/pages/novedadesDetalle;id=6299A6FB-0285-4583-A758-1D3C0B588734)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `FechaInicioSubasta` | fecha | Fecha inicio de la vigencia que asignó la subasta |
| `PrecioCierre` | decimal | Precio de cierre de la subasta o mecanismo correspondiente |
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `CodigoPlanta` | texto | Código de la planta |
| `FechaInicioObligacion` | fecha | Fecha en que inicia la vigencia del periodo cargo |
| `OEFDiaria` | flotante | Vínculo resultante de la subasta o mecanismo del cargo, que impone a un generador el deber de generar, de acuerdo con el  Despacho Ideal, una cantidad diaria de energía durante el Período de Vigencia de la Obligación, cuando el Precio de Bolsa supere  el Precio de Escasez de Activación. Variable discreta no periódica. |
| `FechaFinSubasta` | fecha | Fecha fin de la vigencia que asignó la subasta |
| `PrecioActualizado` | decimal | Valor de precio del cargo por actualizado a valores constante a la fecha de la realización de la publicación |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `TipoSubasta` | texto | Tipo de subasta. Categoría asignada por el ASIC |
| `FechaFinObligacion` | fecha | Fecha en que finaliza la vigencia del periodo cargo |
| `DescripcionSubasta` | texto | Descripción de la subasta |
| `IPPUSABase` | flotante | Índice de precios al productor de los Estados Unidos base |
| `IPPUSADeflactor` | flotante | Índice de precios al productor de los Estados Unidos actual |
| `FechaSubasta` | fecha | Fecha en la que se realizó la última subasta del Cargo por Confiabilidad para el dato correspondiente. Fecha de indexación del IPPUSA base. |
| `Subasta` | texto | Indica el nombre asignado por el ASIC a la subasta |

---

## 18F0B8
### 📊 Información General
**Descripción:** Generación programada por grupo de generación de Redespacho Original, en kWh.

- **Entidad:** XM
- **Categoría:** Generación programada en el redespacho
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-28 22:45:20
- **Última actualización:** 2025-11-27 10:28:52
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 306c67
### 📊 Información General
**Descripción:** Obligaciones de Energía Firme (OEF) de cada planta por cada Período Cargo, por agente y expresada en kWh/año. Tenga en cuenta que la última versión del dato corresponde a la columna FechaPublicacion. Pueden existir nuevas versiones dadas por el cambio de representación del recurso de generación, cesiones, etc. 

- **Entidad:** XM
- **Categoría:** Asignaciones de OEF por planta
- **Periodicidad:** Anual
- **Granularidad:** Anual
- **Fecha de creación:** 2023-09-28 20:52:14
- **Última actualización:** 2025-11-27 00:02:16
- **Próxima actualización:** 2025-12-06 09:00:00
- **Datos históricos:** [https://www.xm.com.co/transacciones/cargo-por-confiabilidad/obligaciones-de-energia-0](https://www.xm.com.co/transacciones/cargo-por-confiabilidad/obligaciones-de-energia-0)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `CodigoPlanta` | texto | Código de la planta |
| `OEF` | decimal | Obligaciones de Energía Firme |
| `FechaFinCargo` | fecha | Fecha en que finaliza la vigencia del periodo cargo |
| `Tecnologia` | texto | Tipo de tecnología que respalda la Obligación de Energía Firme |
| `FechaInicioCargo` | fecha | Fecha en que inicia la vigencia del periodo cargo |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |

---

## 379022
### 📊 Información General
**Descripción:** Indica la hora en la que una planta térmica arranca para el Despacho Ideal

- **Entidad:** XM
- **Categoría:** Bandera de arranque Planta térmica para el Despacho Ideal
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-02-12 14:04:42
- **Última actualización:** 2025-11-27 10:25:18
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [https://www.simem.co/datadetail/fa4671b8-61f8-48df-9817-53f6a711b46b](https://www.simem.co/datadetail/fa4671b8-61f8-48df-9817-53f6a711b46b)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `CodigoPlanta` | texto | Código de la planta |
| `ValorTexto` | texto | Valor de la variable indicada |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 520A3F
### 📊 Información General
**Descripción:** Responsabilidad comercial de AGC (control automático de generación), en COP.

- **Entidad:** XM
- **Categoría:** Responsabilidad comercial de AGC
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-09-05 11:55:41
- **Última actualización:** 2025-11-27 10:30:29
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |
| `Fecha` | fecha | Fecha de representación de la información |

---

## 64eb3f
### 📊 Información General
**Descripción:** Contiene información de Disponibilidad real de las unidades de generación para cada día operativo

- **Entidad:** XM
- **Categoría:** Disponibilidad Real de las Unidades de Generación del Sistema
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-30 21:26:19
- **Última actualización:** 2025-11-27 08:24:23
- **Próxima actualización:** 2025-11-28 08:00:00
- **Datos históricos:** [https://ido.xm.com.co/ido/SitePages/Default.aspx](https://ido.xm.com.co/ido/SitePages/Default.aspx)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `PromedioDisponibilidadReal` | decimal | Energía disponible promedio en los 24 periodos operativos |
| `PorcentajePromedioDisponibilidadReal` | decimal | Porcentaje con respecto a su capacidad efectiva neta de la energía disponible promedio en los 24 periodos operativos |
| `CapacidadEfectivaNeta` | decimal | Capacidad Efectiva Neta de las plantas de generación |
| `TipoGeneracion` | texto | Tipo de clasificación del recurso de generación |
| `CodigoUnidadGeneracion` | texto | Codigo de la unidad de generacion |
| `Fecha` | fecha | Fecha de representación de la información |

---

## 670221
### 📊 Información General
**Descripción:** Contiene el listado de las plantas de generación registradas

- **Entidad:** XM
- **Categoría:** Listado de unidades de generación
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-30 20:19:35
- **Última actualización:** 2025-11-27 09:15:37
- **Próxima actualización:** 2025-11-28 09:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `CodigoPlanta` | texto | Código de la planta |
| `EstadoRecurso` | texto | Estado de la unidad |
| `TipoGeneracion` | texto | Tipo de clasificación del recurso de generación |
| `CodigoUnidadGeneracion` | texto | Codigo de la unidad de generacion |
| `FPO` | fecha | Fecha de Puesta en Operación |
| `NombreUnidad` | texto | Nombre unidad de generacion |
| `Fecha` | fecha | Fecha de representación de la información |

---

## 7BC5F5
### 📊 Información General
**Descripción:** Costo unitario responsabilidad comercial por servicio de control automático de generación, en COP/MBTU.

- **Entidad:** XM
- **Categoría:** Costo unitario responsabilidad comercial de AGC
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-09-05 11:35:15
- **Última actualización:** 2025-11-27 10:26:27
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |
| `Fecha` | fecha | Fecha de representación de la información |

---

## 7F18B1
### 📊 Información General
**Descripción:** Contiene el listado de las plantas de generación registradas que se encuentran en pruebas

- **Entidad:** XM
- **Categoría:** Listado de plantas de generación en pruebas
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2024-05-14 18:43:59
- **Última actualización:** 2025-11-27 08:22:46
- **Próxima actualización:** 2025-11-28 08:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CapacidadEfectivaNeta` | decimal | Capacidad Efectiva Neta de las plantas de generación |
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `NombrePlanta` | texto | Nombre de la planta/recurso de generación |
| `CodigoPlanta` | texto | Código de la planta |
| `CodigoAreaOperativa` | texto | Código del área operativa eléctrica |
| `TipoGeneracion` | texto | Tipo de clasificación del recurso de generación |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `TipoClasificacion` | texto | Clasificación del generador según la regulación actual |
| `CodigoSubAreaOperativa` | texto | Código de la subárea asociada al activo |
| `Fecha` | fecha | Fecha de representación de la información |
| `TipoDespachoRecurso` | texto | Tipo de despacho del recurso |

---

## 7a07ac
### 📊 Información General
**Descripción:** Contiene la información de eventos en las unidades de generación conectadas en el Sistema Interconectado Nacional

- **Entidad:** XM
- **Categoría:** Eventos en unidades de Generación
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-30 23:07:26
- **Última actualización:** 2025-11-27 08:23:52
- **Próxima actualización:** 2025-11-28 08:00:00
- **Datos históricos:** [https://ido.xm.com.co/ido/SitePages/Default.aspx](https://ido.xm.com.co/ido/SitePages/Default.aspx)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CapacidadEfectivaNeta` | decimal | Capacidad Efectiva Neta de las plantas de generación |
| `EventoGenerador` | texto | NULL |
| `DescripcionEvento` | texto | NULL |
| `TipoCombustible` | texto | Tipo Combustible |
| `EstadoGenerador` | texto | Estado de la unidad a partir del evento registrado |
| `DisponibilidadEnergia` | decimal | Disponibilidad de energía declarada por la unidad de generación |
| `CodigoUnidadGeneracion` | texto | Codigo de la unidad de generacion |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 8DECCA
### 📊 Información General
**Descripción:** Cantidades y precios promedios de los contratos registrados del Mercado Secundario para el cargo por confiabilidad. El precio promedio ponderado se pondera por la cantidad de energía comprometida en cada contrato.

- **Entidad:** XM
- **Categoría:** Estadísticas de contratos del mercado secundario
- **Periodicidad:** Mensual
- **Granularidad:** Mensual
- **Fecha de creación:** 2023-09-30 11:35:39
- **Última actualización:** 2025-11-27 09:34:13
- **Próxima actualización:** 2025-11-28 08:00:00
- **Datos históricos:** [https://www.xm.com.co/transacciones/cargo-por-confiabilidad/informacion-de-los-contratos-del-mercado-secundario](https://www.xm.com.co/transacciones/cargo-por-confiabilidad/informacion-de-los-contratos-del-mercado-secundario)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `PPP_USDMWh` | decimal | Precio Promedio Ponderado por la variable indicada en la descripción del conjunto de datos en USD/MWh |
| `NumeroDeContratos` | entero | Número total de contratos |
| `PPS_COPkWh` | decimal | Precio Promedio Simple en COP/kWh |
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `VCMSTotales` | decimal | Ventas en Contratos del Mercado Secundario totales (ENFICC + EDA) |
| `PPS_USDMWh` | decimal | Precio Promedio Simple en USD/MWh |
| `ENFICC` | decimal | Energía Firme del Cargo por Confiabilidad |
| `EDA` | decimal | Energía Disponible Adicional |
| `RespaldoConPlantasPropias` | texto | Indica "Si" para los contratos donde la planta que compra y la planta que vende pertenecen al mismo agente, de lo contrario es "No" |
| `PPP_COPkWh` | decimal | Precio Promedio Ponderado por la variable indicada en la descripción del conjunto de datos en COP/kWh |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |
| `Fecha` | fecha | Fecha de representación de la información |

---

## 909809
### 📊 Información General
**Descripción:** Contiene los precios de oferta de Arranque y parada por recurso reportados de forma trimestral al CND

- **Entidad:** XM
- **Categoría:** Precio de Oferta de Arranque y Parada por recurso USD
- **Periodicidad:** Trimestral
- **Granularidad:** Mensual
- **Fecha de creación:** 2023-09-29 18:04:08
- **Última actualización:** 2025-07-29 20:35:51
- **Próxima actualización:** 2025-08-01 07:00:00
- **Datos históricos:** [NaN](NaN)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Configuracion` | texto | Número de la configuración asociado al recurso de generación |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## 9E77E5
### 📊 Información General
**Descripción:** Disponibilidad Real por cada recurso de Generación, en kWh.

- **Entidad:** XM
- **Categoría:** Disponibilidad real
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-03-07 11:17:46
- **Última actualización:** 2025-11-27 10:25:59
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## BE51B1
### 📊 Información General
**Descripción:** Contiene 19 variables que describen Obligaciones de energía firme, precios del Cargo por Confiabilidad, entre otros

- **Entidad:** XM
- **Categoría:** Obligación de energía firme por submercado
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-07-07 14:21:07
- **Última actualización:** 2025-11-27 10:27:35
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [https://www.simem.co/datadetail/fa4671b8-61f8-48df-9817-53f6a711b46b](https://www.simem.co/datadetail/fa4671b8-61f8-48df-9817-53f6a711b46b)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## E055B4
### 📊 Información General
**Descripción:** Generación programada por grupo de generación de despacho Original, en kWh.

- **Entidad:** XM
- **Categoría:** Generación programada en el despacho
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-28 22:45:20
- **Última actualización:** 2025-11-27 10:23:11
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## E17D25
### 📊 Información General
**Descripción:** Contiene para las plantas del Sistema Interconectado Nacional (SIN) generación programada en el despacho, generación programada en el redespacho y generación real.

- **Entidad:** XM
- **Categoría:** Generación Real y Programada en las Plantas de Generación
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-29 10:59:40
- **Última actualización:** 2025-11-27 11:21:40
- **Próxima actualización:** 2025-11-28 11:00:00
- **Datos históricos:** [https://ido.xm.com.co/ido/SitePages/Default.aspx](https://ido.xm.com.co/ido/SitePages/Default.aspx)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `GeneracionRealEstimada` | decimal | Generación real estimada a través del SCADA |
| `GeneracionProgramadaRedespacho` | decimal | Generación programada en el redespacho |
| `CodigoPlanta` | texto | Código de la planta |
| `TipoGeneracion` | texto | Tipo de clasificación del recurso de generación |
| `TipoClasificacion` | texto | Clasificación del generador según la regulación actual |
| `GeneracionProgramadaDespacho` | decimal | Generación programada en el despacho económico |
| `Fecha` | fecha | Fecha de representación de la información |
| `TipoDespachoRecurso` | texto | Tipo de despacho del recurso |

---

## EC6945
### 📊 Información General
**Descripción:** Precio de bolsa horario nacional, internacional y TIE

- **Entidad:** XM
- **Categoría:** Precio de bolsa horario
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-10-02 21:36:52
- **Última actualización:** 2025-11-27 10:28:26
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## F28855
### 📊 Información General
**Descripción:** Contiene la información histórica de eventos en las unidades de generación conectadas en el Sistema Interconectado Nacional

- **Entidad:** XM
- **Categoría:** Histórico de eventos en Unidades de Generación
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-28 20:53:27
- **Última actualización:** 2025-11-27 07:20:04
- **Próxima actualización:** 2025-11-28 07:00:00
- **Datos históricos:** [https://ido.xm.com.co/ido/SitePages/Default.aspx](https://ido.xm.com.co/ido/SitePages/Default.aspx)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CapacidadEfectivaNeta` | decimal | Capacidad Efectiva Neta de las plantas de generación |
| `EventoGenerador` | texto | NULL |
| `DescripcionEvento` | texto | NULL |
| `TipoCombustible` | texto | Tipo Combustible |
| `EstadoGenerador` | texto | Estado de la unidad a partir del evento registrado |
| `DisponibilidadEnergia` | decimal | Disponibilidad de energía declarada por la unidad de generación |
| `CodigoUnidadGeneracion` | texto | Codigo de la unidad de generacion |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## F3A9B1
### 📊 Información General
**Descripción:** Contiene las banderas donde el Centro Nacional de Despacho indica si la planta tuvo un evento que afectó la disponibilidad. Este valor se considera posteriormente para determinar la Disponibilidad Comercial calculada por el Administrador del Sistema de Intercambios Comerciales

- **Entidad:** XM
- **Categoría:** Bandera de Disponibilidad Real
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2025-03-07 11:17:46
- **Última actualización:** 2025-11-27 10:26:38
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `CodigoPlanta` | texto | Código de la planta |
| `ValorTexto` | texto | Valor de la variable indicada |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## ab3d66
### 📊 Información General
**Descripción:** Contiene la información soporte a la liquidación realizada por el Administrador del Sistema de Intercambios Comerciales (ASIC) del proceso de Contratos por versión y horaria

- **Entidad:** XM
- **Categoría:** Datos soporte del proceso de Contratos por versión y horaria
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-29 00:26:01
- **Última actualización:** 2025-11-27 10:24:23
- **Próxima actualización:** 2025-11-28 10:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `Version` | texto | Versión de la liquidación |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## b38efc
### 📊 Información General
**Descripción:** Presenta la información de la Energía en Firme del Cargo por Confiabilidad que ha sido verificada por el Centro Nacional de Despacho para cada planta de generación

- **Entidad:** XM
- **Categoría:** Energía Firme del Cargo por Confiabilidad verificada por el Centro Nacional de Despacho
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-30 18:03:55
- **Última actualización:** 2025-11-27 09:13:02
- **Próxima actualización:** 2025-11-28 09:00:00
- **Datos históricos:** [https://stsimemprd01.blob.core.windows.net/simem/SIMEM/InfoCargoPorConfiabilidad/ENFICCVerificada?sp=r&st=2023-09-29T20:28:31Z&se=2023-09-30T04:28:31Z&spr=https&sv=2022-11-02&sr=b&sig=yuG82iqyGFqfILrSYLXImeFVR+JoXPwPFg4bT8nQYfs=](https://stsimemprd01.blob.core.windows.net/simem/SIMEM/InfoCargoPorConfiabilidad/ENFICCVerificada?sp=r&st=2023-09-29T20:28:31Z&se=2023-09-30T04:28:31Z&spr=https&sv=2022-11-02&sr=b&sig=yuG82iqyGFqfILrSYLXImeFVR+JoXPwPFg4bT8nQYfs=)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `FechaFin` | fecha | Fecha final de vigencia del dato |
| `FechaPublicacion` | fecha | Fecha de publicación del dato en el SIMEM |
| `CodigoPlanta` | texto | Código de la planta |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `ENFICCVerificada` | decimal | Energía Firme del Cargo por Confiabilidad - ENFICC verificada |
| `Fecha` | fecha | Fecha de representación de la información |

---

## cf0167
### 📊 Información General
**Descripción:** Costo de las restricciones del Sistema de Transmisión Nacional (STN), aplicables a los agentes comercializadores.

- **Entidad:** XM
- **Categoría:** Costo Restricciones Asignadas al Agente
- **Periodicidad:** Mensual
- **Granularidad:** Mensual
- **Fecha de creación:** 2023-09-26 08:53:41
- **Última actualización:** 2025-11-19 20:24:42
- **Próxima actualización:** 2026-12-05 23:00:00
- **Datos históricos:** [NaN](NaN)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## e427a2
### 📊 Información General
**Descripción:** Contiene los precios de oferta de arranque y parada diarios en USD declarados al CND por parte de las Unidades de generación

- **Entidad:** XM
- **Categoría:** Precio oferta arranque y parada por unidad para el combustible USD
- **Periodicidad:** Mensual
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-29 16:56:36
- **Última actualización:** 2025-11-05 07:29:30
- **Próxima actualización:** 2025-11-05 07:00:00
- **Datos históricos:** [NA](NA)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `EstadoTermico` | texto | Estado térmico de la unidad |
| `TipoCombustible` | texto | Tipo Combustible |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `CodigoSICAgente` | texto | Código del agente asignado por el ASIC |
| `CodigoUnidadGeneracion` | texto | Codigo de la unidad de generacion |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## ea1c85
### 📊 Información General
**Descripción:** Contiene información de la reserva asignada por periodo a las plantas de generación para prestar el servicio de control de frecuencia denominado Control Automático de Generación (AGC por sus siglas en inglés)

- **Entidad:** XM
- **Categoría:** Reserva asignada como Control Automático de Generación
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-30 18:49:51
- **Última actualización:** 2025-11-27 08:24:46
- **Próxima actualización:** 2025-11-28 08:00:00
- **Datos históricos:** [https://ido.xm.com.co/ido/SitePages/Default.aspx](https://ido.xm.com.co/ido/SitePages/Default.aspx)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoElementoGeneracion` | texto | Código del Elemento de Generación: Planta o Unidad |
| `MargenAGCArriba` | flotante | Holgura de regulación de frecuencia secundaria hacia arriba |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |
| `MargenAGCAbajo` | flotante | Holgura de regulación de frecuencia secundaria hacia abajo |

---

## fa4671
### 📊 Información General
**Descripción:** Contiene la información soporte a la liquidación realizada por el Administrador del Sistema de Intercambios Comerciales (ASIC) del proceso de Contratos por Recurso, versión y diaria

- **Entidad:** XM
- **Categoría:** Datos soporte del proceso de Contratos por Recurso, versión y diaria
- **Periodicidad:** Diaria
- **Granularidad:** Diaria
- **Fecha de creación:** 2023-09-28 22:04:50
- **Última actualización:** 2025-11-19 20:25:03
- **Próxima actualización:** 2025-11-20 09:00:00
- **Datos históricos:** [NA](NA)

#### 📢 Última Novedad
**Finalización de conjunto de datos con corte al 2025-09-11**

*Finalización conjunto de datos 2025-09-11*

Como parte del proceso de mejora continua en la actualización y consulta de variables relacionadas con el Mercado de Energía Mayorista y la operación del Sistema Interconectado Nacional, SIMEM informa que a partir del 2025-09-11 quedarán finalizados 3 conjuntos de datos, Datos soporte del proceso de Demandas por Recurso, versión y diaria, Datos soporte del proceso de Contratos por Recurso, versión y diaria y Datos soporte del proceso de liquidación por Recurso, versión y diaria.

- **Fecha:** 2025-09-11
- **Más información:** [https://www.simem.co/pages/novedadesDetalle;id=B5BBC16C-6068-4615-F244-08DDF2071B82](https://www.simem.co/pages/novedadesDetalle;id=B5BBC16C-6068-4615-F244-08DDF2071B82)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `CodigoVariable` | texto | Código de la variable |
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoPlanta` | texto | Código de la planta |
| `UnidadMedida` | texto | Unidad de medida en la que se encuentra la variable |
| `FechaInicio` | fecha | Fecha de inicio del dato |
| `Version` | texto | Versión de la liquidación |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

## ff027b
### 📊 Información General
**Descripción:** Contiene el programa de generación del despacho económico en kW

- **Entidad:** XM
- **Categoría:** Despacho programado recursos de generación
- **Periodicidad:** Diaria
- **Granularidad:** Horaria
- **Fecha de creación:** 2023-09-30 10:52:26
- **Última actualización:** 2025-11-27 16:17:28
- **Próxima actualización:** 2025-11-28 16:00:00
- **Datos históricos:** [https://www.xm.com.co/corto-plazo/despacho-energia/informe-del-despacho](https://www.xm.com.co/corto-plazo/despacho-energia/informe-del-despacho)

### 📋 Estructura de Datos (Columnas)
| Columna | Tipo de Dato | Descripción |
|---------|--------------|-------------|
| `Valor` | decimal | Valor de la variable (escala de 4 cifras) |
| `CodigoElementoGeneracion` | texto | Código del Elemento de Generación: Planta o Unidad |
| `FechaHora` | fecha hora | Fecha y hora de representación del dato |
| `CodigoDuracion` | texto | Código de duración de la variable en formato ISO8601 |

---

