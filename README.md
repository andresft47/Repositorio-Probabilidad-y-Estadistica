# Proyecto de Probabilidad y Estadística

Este repositorio contiene diversos módulos y scripts en Python desarrollados para el estudio y aplicación de conceptos de probabilidad y estadística. El proyecto se organiza en tres apartados principales, cada uno ubicado en su respectiva carpeta.

## Estructura del Proyecto

### 1. Probabilidad
**Carpeta:** `Probabilidad/`

Este apartado se enfoca en la visualización de distribuciones y conceptos fundamentales de probabilidad.

*   **`DistribucionesProbabilidad.py`**: Genera visualizaciones para distribuciones fundamentales:
    *   **Binomial**: Éxitos en ensayos independientes.
    *   **Poisson**: Eventos en intervalos fijos.
    *   **Normal Estándar**: Campana de Gauss con media 0 y desviación estándar 1.
*   **`Probabilidad_Conjunta.py`**: Utiliza gráficos 3D para ilustrar:
    *   Probabilidad conjunta de lanzar dados.
    *   Funciones de densidad uniforme.
    *   Regiones de probabilidad (ej. `x + y <= 1`).

### 2. Muestreo
**Carpeta:** `Muestreo/`

Enfocado en el manejo de datos y técnicas de recolección de muestras a partir de una población.

*   **`muestreo.py`**: Implementa técnicas de **muestreo sistemático** sobre un conjunto de datos, comparando estadísticas (promedio, distribución) entre la muestra y la población total.
*   **`normalizacion_dataset.py`**: Script para la limpieza y estandarización del dataset original para asegurar consistencia en los análisis.
*   **`poblacion_videojuegos.csv`**: Base de datos de jugadores y sus gastos en compras integradas, utilizada como población para los ejercicios de muestreo.

### 3. Proyecto de Estadística (Control de Gastos)
**Carpeta:** `ProyectoEstadistica/`

Aplicación práctica de la estadística descriptiva en un sistema de gestión financiera personal.

*   **`CodigoProyecto.py`**: Sistema de "Control de Gastos Universitarios" que permite:
    *   Registrar gastos por categorías (Alimentación, Transporte, etc.).
    *   Calcular el nivel de riesgo financiero basado en el ingreso mensual.
    *   Generar estadísticas descriptivas (promedio, desviación estándar, valor máximo).
    *   Visualizar la distribución de gastos mediante diagramas de barras.

## Requisitos
Para ejecutar los scripts de este repositorio, asegúrese de tener instaladas las siguientes librerías:
*   **NumPy**: Para cálculos numéricos.
*   **Pandas**: Para manipulación y análisis de datos.
*   **Matplotlib**: Para la generación de gráficos y visualizaciones.
*   **SciPy**: Para funciones estadísticas avanzadas.

---
*Desarrollado como parte del curso de Probabilidad y Estadística.*
