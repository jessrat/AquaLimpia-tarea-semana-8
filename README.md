# Análisis de Desempeño: Plantas de Tratamiento AquaLimpia S.A.

---

## 1. Objetivo del Proyecto
El objetivo del proyecto es analizar el desempeño operacional de las plantas de tratamiento de aguas residuales de **AquaLimpia S.A.** con el fin de evaluar:
* La **eficiencia** del proceso de depuración.
* El grado de **cumplimiento normativo** ambiental.
* El comportamiento del **consumo energético**.

---

## 2. Fuente de Datos
la fuente de dartos es el archivo Excel `dataset_set_A_aguas_residuales.xlsx`, y contiene datos operacionales de las plantas en las siguientes columnas:

> * **Identificación de planta:** Nombre de la planta.
> * **Caudal de entrada:** Volumen de agua ingresado ($m^3/\text{día}$).
> * **DBO de entrada y salida:** Demanda Bioquímica de Oxígeno ($mg/L$).
> * **Energía de aireación:** Consumo energético ($kWh$).
> * **Lodos generados:** Subproductos del proceso ($kg/\text{día}$).
> * **Cumplimiento de norma:** Norma ambiental (1 = Cumple / 0 = No cumple).

---

## 3. Proceso Analítico (Workflow)
El desarrollo del análisis en este Notebook se divide en las siguientes etapas:

1.  **Importación de Datos:** Carga del archivo Excel al entorno de ejecución de Google Colab utilizando la librería `pandas`.
2.  **Evaluación de Calidad:** Identificar y eliminar valores nulos, registros duplicados o inconsistencias.
3.  **Limpieza y Preparación:** Estandarización de nombres de columnas y completar datos faltantes.
4.  **Métricas:** Cálculo de indicadores de negocio adicionales:
    * *Eficiencia del tratamiento* ($\%$ de remoción de DBO).
    * *Consumo energético específico* ($kWh/m^3$).
    * *Indicadores globales de cumplimiento*.
5.  **Agrupación:** Agrupación de datos por planta.
6.  **Visualización (Dashboard):** Construcción de gráficos interactivos utilizando `matplotlib` y `seaborn`:
    * Caudal promedio por instalación.
    * Tasa porcentual de cumplimiento de norma.
    * Distribución de la eficiencia del tratamiento.
    * Dispersión y relación matemática entre *Energía* vs *Caudal*.

---

## 4. Resultados Clave
el análisis del dashboard, identifico los siguientes hallazgos:
* **Variabilidad en Eficiencia:** •	Se aprecian diferencias de eficiencia entre las plantas.
* **Alertas de Cumplimiento:** •	hay plantas con bajo cumplimiento normativo.
* **Comportamiento Energético:** •	El consumo de energía varía según el caudal.
* **Optimización:** Se aprecia oportunidades de mejora en los procesos.

---

## 5. Conclusiones
el análisis permite detectar problemas normativos y de desempeño de las plantas, con la información obtenida se puede elaborar un **plan de mejora** para cumplir con las normativas ambientales y mejorar la eficiencia.

---

## 6. Reproducibilidad y Gobierno de Código
Con el fin de garantizar que este análisis pueda ser auditado o automatizado en el futuro:
* La lógica de código se encapsuló en **funciones de Python modulares**.
* El control de versiones y el almacenamiento de los scripts se gestiona a través de un **repositorio en GitHub**.
