# 🎮 Análisis de Ventas Globales de Videojuegos
### Planificación Estratégica para 2017 — Data Science Portfolio Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Hypothesis%20Testing-8CAAE6?logo=scipy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?logo=seaborn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?logo=matplotlib)
![Jupyter](https://img.shields.io/badge/Jupyter-Reproducible%20Analysis-F37626?logo=jupyter&logoColor=white)

---

## 📌 Resumen ejecutivo

Este proyecto analiza el comportamiento histórico del mercado global de videojuegos utilizando información de ventas, plataformas, géneros, reseñas de usuarios y críticos, clasificación ESRB y desempeño regional.

El objetivo principal es transformar datos históricos en **insights accionables para la planificación comercial y publicitaria de la tienda online Ice para 2017**.

El análisis aborda tres dimensiones principales:

- **Comportamiento temporal:** evolución de plataformas y ciclos de vida.
- **Factores asociados al éxito comercial:** ventas, reseñas, géneros y desempeño multiplataforma.
- **Diferencias regionales:** comportamiento de los mercados de Norteamérica (NA), Europa (EU) y Japón (JP).

Además del análisis exploratorio, se incorporan **pruebas estadísticas de hipótesis mediante la prueba t de Welch**, buscando diferenciar patrones descriptivos de relaciones estadísticamente significativas.

> **Enfoque:** Data Science aplicada a la toma de decisiones de negocio.

---

# 🎯 Objetivo de negocio

La industria de videojuegos presenta ciclos tecnológicos cortos, fuertes efectos de popularidad y diferencias significativas entre regiones.

La pregunta central del proyecto es:

> **¿Qué características permiten identificar los videojuegos y plataformas con mayor potencial comercial para orientar la estrategia de marketing de Ice durante 2017?**

A partir de esta pregunta se plantearon los siguientes objetivos:

1. Identificar las plataformas con mayor potencial comercial.
2. Analizar el ciclo de vida de las principales plataformas.
3. Determinar la relación entre reseñas y ventas.
4. Evaluar el comportamiento de títulos multiplataforma.
5. Identificar los géneros con mayor volumen y rentabilidad relativa.
6. Comparar las preferencias de los mercados NA, EU y JP.
7. Evaluar estadísticamente diferencias entre grupos mediante pruebas de hipótesis.
8. Traducir los resultados en recomendaciones estratégicas para 2017.

---

# 🧠 Enfoque analítico

El proyecto sigue un flujo reproducible de análisis:

```text
Datos originales
      │
      ▼
Calidad y limpieza de datos
      │
      ▼
Transformación y consolidación
      │
      ▼
Análisis exploratorio (EDA)
      │
      ├── Plataformas
      ├── Ciclo de vida
      ├── Géneros
      ├── Reseñas
      └── Ventas
      │
      ▼
Segmentación regional
      │
      ├── Norteamérica
      ├── Europa
      └── Japón
      │
      ▼
Pruebas estadísticas
      │
      ▼
Interpretación de resultados
      │
      ▼
Recomendaciones de negocio
```

---

# 📂 Estructura del repositorio

```text
├── data/
│   └── games.csv
│
├── notebooks/
│   └── analisis_videojuegos.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── metrics.py
│   └── hypotheses.py
│
├── requirements.txt
│
└── README.md
```

### Componentes principales

| Archivo | Responsabilidad |
|---|---|
| `data/games.csv` | Dataset original |
| `notebooks/analisis_videojuegos.ipynb` | Análisis exploratorio, visualizaciones y conclusiones |
| `src/preprocessing.py` | Limpieza, transformación y consolidación |
| `src/metrics.py` | Métricas y análisis descriptivo |
| `src/hypotheses.py` | Pruebas estadísticas |
| `requirements.txt` | Dependencias del proyecto |
| `README.md` | Documentación y resultados |

La separación entre **procesamiento, métricas, inferencia estadística y presentación** permite mantener una arquitectura más mantenible y reutilizable que concentrar toda la lógica en un único notebook.

---

# 🧹 1. Preparación y calidad de datos

El primer componente del proyecto está orientado a garantizar la calidad de la información antes de realizar inferencias.

### Procesos realizados

- Estandarización de nombres de variables mediante `snake_case`.
- Conversión de variables numéricas.
- Tratamiento de valores `TBD` como valores ausentes.
- Conservación de valores faltantes reales.
- Validación de tipos de datos.
- Consolidación de registros fragmentados.
- Creación de la métrica:

```text
total_sales =
NA_sales +
EU_sales +
JP_sales +
Other_sales
```

### Tratamiento de valores faltantes

Los valores `TBD` fueron convertidos a `NaN` en lugar de imputarse automáticamente.

Esta decisión busca evitar introducir información artificial en variables relacionadas con:

- `user_score`
- `critic_score`
- `year_of_release`

La ausencia de información se conserva explícitamente para evitar sesgos derivados de imputaciones no justificadas.

---

# 📅 2. Definición de la ventana temporal

El dataset contiene información histórica desde aproximadamente 1980.

Inicialmente se realizó una revisión longitudinal del mercado para identificar cambios estructurales en la industria.

El análisis mostró:

- Incremento de producción hacia 2008–2009.
- Posterior transición tecnológica.
- Consolidación de la octava generación de consolas.
- Aparición y expansión de plataformas como PS4 y Xbox One.

Por este motivo, se definió **2012–2016 como ventana principal de análisis**, debido a que permite capturar la dinámica más relevante para la planificación comercial de 2017.

### Plataformas relevantes

- PlayStation 4 (`PS4`)
- Xbox One (`XOne`)
- PlayStation 3 (`PS3`)
- Xbox 360 (`X360`)
- Nintendo 3DS (`3DS`)
- PlayStation Vita (`PSV`)
- Wii U

---

# 📊 3. Análisis exploratorio

## 3.1 Ciclo de vida de plataformas

El análisis temporal permitió identificar patrones relativamente consistentes en la evolución comercial de las plataformas.

### Hallazgos

- Una plataforma tarda aproximadamente **10–11 años** en completar su ciclo de vida.
- El máximo nivel de ventas suele aparecer aproximadamente entre **3 y 5 años después del lanzamiento**.
- PS4 y Xbox One representan las plataformas de sobremesa con mayor potencial comercial dentro de la ventana analizada.
- PS3 y Xbox 360 muestran señales de transición hacia el declive generacional.

Este comportamiento resulta especialmente relevante para la planificación de inversión publicitaria, ya que permite distinguir entre plataformas en expansión, madurez y declive.

---

# 📈 4. Distribución de ventas y efecto de los blockbusters

El análisis de dispersión muestra un patrón de **asimetría positiva**.

En las principales plataformas:

> **Media de ventas > Mediana de ventas**

Esto indica que una pequeña cantidad de videojuegos con ventas extraordinariamente altas tiene una influencia considerable sobre el promedio.

### Implicación de negocio

El promedio por sí solo puede sobreestimar el desempeño típico de un videojuego.

Por esta razón, el análisis incorpora medidas robustas como:

- Mediana.
- Percentiles.
- Distribución de ventas.
- Boxplots.
- Identificación de valores extremos.

Esto permite distinguir entre:

```text
Desempeño típico
        vs.
Éxito excepcional de blockbusters
```

---

# ⭐ 5. Reseñas y ventas

Se evaluó la relación entre las calificaciones de críticos (`critic_score`), las calificaciones de usuarios (`user_score`) y las ventas.

## Xbox 360

Los resultados muestran:

| Variable | Correlación aproximada con ventas |
|---|---:|
| `critic_score` | **0.36** |
| `user_score` | **-0.01** |

### Interpretación

Existe una **correlación positiva moderada** entre las calificaciones de críticos y las ventas.

Los títulos con puntuaciones superiores a 80 presentan, en términos generales, un mejor desempeño comercial.

En contraste, la correlación prácticamente nula entre `user_score` y ventas sugiere que la valoración de usuarios no presenta una relación lineal clara con las ventas en esta plataforma.

> Importante: correlación no implica causalidad. Los resultados identifican asociación estadística, no un efecto causal de las reseñas sobre las ventas.

---

# 🔄 6. Análisis multiplataforma

Se comparó el desempeño comercial de títulos lanzados simultáneamente en Xbox 360 y PlayStation 3.

La correlación de ventas observada fue superior a:

> **r > 0.85**

Esto representa una asociación lineal muy fuerte.

### Insight estratégico

Cuando un mismo título está disponible en plataformas competidoras, su desempeño tiende a moverse de forma similar.

Esto sugiere que factores como:

- fuerza de la franquicia,
- reconocimiento de marca,
- género,
- calidad del producto,
- campaña de marketing,

pueden tener mayor relevancia comercial que la plataforma específica.

### Implicación

Los títulos de alto potencial deberían evaluarse desde una perspectiva **multiplataforma**, especialmente cuando el mercado objetivo incluye simultáneamente usuarios de PlayStation y Xbox.

---

# 🎮 7. Análisis por género

Se evaluaron los géneros considerando tanto el volumen total como el rendimiento relativo por título.

### Volumen total

**Action** lidera las ventas acumuladas:

- Aproximadamente **441 millones de unidades**.
- Aproximadamente **1.031 títulos**.

Sin embargo, el volumen total no necesariamente representa mayor eficiencia comercial.

### Rentabilidad relativa

**Shooter** presenta un desempeño superior en términos de ventas por título, mostrando una mayor mediana y promedio unitario.

Esto permite diferenciar:

```text
Volumen de mercado
        vs.
Rendimiento por título
```

### Insight

Action representa un mercado de gran escala y alta competencia.

Shooter, aunque presenta menor cantidad de títulos que Action, muestra mayor potencial de rendimiento individual.

---

# 🌎 8. Segmentación regional

Se analizaron tres mercados principales:

- 🇺🇸 Norteamérica (`NA`)
- 🇪🇺 Europa (`EU`)
- 🇯🇵 Japón (`JP`)

La segmentación permitió identificar diferencias importantes en:

- Plataformas.
- Géneros.
- Preferencias culturales.
- Clasificación de videojuegos.

---

## 🇺🇸 Norteamérica

### Principales plataformas

| Plataforma | Participación aproximada |
|---|---:|
| X360 | 23.7% |
| PS4 | 18.4% |
| PS3 | 17.5% |
| XOne | 15.8% |

### Géneros predominantes

- Action
- Shooter
- Sports
- Role-Playing

### Clasificación ESRB

| Rating | Participación |
|---|---:|
| M | 39.2% |
| E | 19.4% |
| E10+ | 12.8% |

---

# 🇪🇺 Europa

### Principales plataformas

| Plataforma | Participación aproximada |
|---|---:|
| PS4 | 27.8% |
| PS3 | 21.1% |
| X360 | 14.7% |
| XOne | 10.2% |

### Géneros predominantes

- Action
- Shooter
- Sports
- Role-Playing

### Clasificación ESRB

| Rating | Participación |
|---|---:|
| M | 38.3% |
| E | 22.3% |
| E10+ | 10.9% |

---

# 🇯🇵 Japón

Japón presenta un patrón significativamente diferente respecto a los mercados occidentales.

### Principales plataformas

| Plataforma | Participación aproximada |
|---|---:|
| 3DS | 45.6% |
| PS3 | 18.3% |
| PSV | 10.9% |

La participación de Xbox es prácticamente marginal.

### Géneros

El mercado japonés muestra una fuerte orientación hacia:

- Role-Playing
- JRPG
- Action

Los géneros occidentales como Shooter tienen una presencia considerablemente menor dentro de los principales segmentos.

### Clasificación

La clasificación ESRB no representa adecuadamente el mercado japonés, donde existen sistemas regulatorios y de clasificación locales.

Por este motivo, los valores `Unknown` deben interpretarse con cautela y no necesariamente como ausencia de clasificación.

---

# 🧪 9. Inferencia estadística

Para evitar basar las conclusiones únicamente en diferencias descriptivas, se realizaron pruebas de hipótesis.

Se utilizó:

> **Prueba t de Welch para dos muestras independientes**

con:

```text
alpha = 0.05
equal_var = False
```

La elección de Welch permite comparar medias sin asumir igualdad de varianzas entre los grupos.

---

# 📐 10. Hipótesis 1 — Xbox One vs. PC

Se compararon las calificaciones promedio de usuarios entre Xbox One y PC.

### Hipótesis

**H₀:**

> Las calificaciones promedio de usuarios son iguales.

**H₁:**

> Las calificaciones promedio de usuarios son diferentes.

### Resultado

| Plataforma | Media |
|---|---:|
| PC | 7.06 |
| Xbox One | 6.52 |

El resultado produjo:

> **p < 0.05**

### Conclusión

Se **rechaza H₀**.

Existe evidencia estadística suficiente para afirmar que las calificaciones promedio de usuarios difieren entre PC y Xbox One.

---

# 📐 11. Hipótesis 2 — Action vs. Sports

Se compararon las calificaciones promedio de usuarios entre los géneros Action y Sports.

### Hipótesis

**H₀:**

> Las calificaciones promedio son iguales.

**H₁:**

> Las calificaciones promedio son diferentes.

### Resultado

```text
p = 0.0775
alpha = 0.05
```

Como:

```text
p > alpha
```

### Conclusión

**No se rechaza H₀.**

No existe evidencia estadística suficiente, al nivel de significancia del 5%, para afirmar que las calificaciones promedio de usuarios entre Action y Sports sean diferentes.

---

# 💡 12. Recomendaciones estratégicas para 2017

Los resultados se traducen en las siguientes recomendaciones de negocio.

## 1. Priorizar la octava generación en Occidente

Para Norteamérica y Europa:

- Priorizar PS4 y Xbox One.
- Reducir progresivamente la inversión en PS3 y Xbox 360.
- Favorecer lanzamientos con estrategia multiplataforma.

La estrategia debe considerar el ciclo de vida de las plataformas y no únicamente sus ventas históricas.

---

## 2. Apostar por títulos AAA de alto potencial

Los resultados muestran una industria caracterizada por una distribución altamente asimétrica.

Por ello, la estrategia debe identificar títulos con:

- Alto potencial de ventas.
- Buen desempeño crítico.
- Reconocimiento de franquicia.
- Distribución multiplataforma.
- Géneros con alto rendimiento.

Los géneros prioritarios en mercados occidentales serían:

**Shooter + Action + Sports**

---

## 3. Utilizar las reseñas críticas como indicador complementario

La correlación positiva observada entre `critic_score` y ventas sugiere utilizar la evaluación crítica como una variable complementaria para priorizar campañas.

Una posible regla de segmentación sería:

```text
critic_score > 80
        +
plataforma de nueva generación
        +
género de alto potencial
        +
franquicia consolidada
        ↓
Alta prioridad de marketing
```

Esta regla debe utilizarse como mecanismo de priorización, no como modelo causal.

---

## 4. Estrategia diferenciada para Japón

Japón requiere una estrategia independiente.

Las prioridades deberían centrarse en:

- Nintendo 3DS.
- PlayStation Vita.
- Juegos Role-Playing.
- JRPG.
- Desarrolladores y franquicias locales.

No se recomienda extrapolar directamente el comportamiento de NA/EU al mercado japonés.

---

# 📌 13. Principales insights de negocio

| Insight | Implicación |
|---|---|
| PS4/XOne lideran la nueva generación | Priorizar inversión occidental |
| Las ventas presentan fuerte asimetría | Usar mediana y percentiles además del promedio |
| `critic_score` presenta relación positiva con ventas | Utilizar reseñas críticas como indicador complementario |
| `user_score` muestra relación débil en X360 | No utilizarlo como único criterio de inversión |
| Ventas X360/PS3 presentan correlación > 0.85 | Potenciar estrategia multiplataforma |
| Action domina por volumen | Mercado grande pero altamente competido |
| Shooter presenta mayor rendimiento por título | Potencial atractivo para campañas |
| Japón tiene fuerte concentración en 3DS | Estrategia regional diferenciada |
| Japón presenta preferencia por RPG/JRPG | Priorizar contenido adaptado al mercado local |

---

# 🏗️ 14. Arquitectura del proyecto

El proyecto fue estructurado para separar responsabilidades.

### `preprocessing.py`

Responsable de:

- Limpieza.
- Normalización.
- Conversión de tipos.
- Tratamiento de valores faltantes.
- Consolidación de registros.

### `metrics.py`

Responsable de:

- Métricas de ventas.
- Análisis de plataformas.
- Ciclos de vida.
- Análisis por género.
- Perfiles regionales.
- Correlaciones.

### `hypotheses.py`

Responsable de:

- Pruebas de hipótesis.
- Prueba t de Welch.
- Cálculo de resultados estadísticos.
- Formateo de resultados.

### Notebook

El notebook funciona como capa de:

- Exploración.
- Visualización.
- Interpretación.
- Comunicación de resultados.

La lógica reutilizable se mantiene fuera del notebook para mejorar la mantenibilidad del proyecto.

---

# 🧰 15. Stack tecnológico

### Lenguaje

- Python 3.10+

### Manipulación de datos

- Pandas
- NumPy

### Estadística

- SciPy

### Visualización

- Matplotlib
- Seaborn

### Entorno

- Jupyter Notebook

### Buenas prácticas

- Modularización.
- Reproducibilidad.
- Separación de responsabilidades.
- Tratamiento explícito de datos faltantes.
- Validación estadística.
- Comunicación de resultados de negocio.

---

# ▶️ 16. Ejecución del proyecto

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno en Windows:

```bash
.venv\Scripts\activate
```

Activar en macOS/Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar Jupyter:

```bash
jupyter notebook
```

Abrir:

```text
notebooks/analisis_videojuegos.ipynb
```

---

# 📊 17. Resultados esperados

El proyecto permite responder preguntas como:

- ¿Qué plataformas presentan mayor potencial comercial?
- ¿En qué etapa del ciclo de vida se encuentra cada consola?
- ¿Qué géneros generan mayor volumen?
- ¿Qué géneros presentan mayor rendimiento por título?
- ¿Existe relación entre calidad crítica y ventas?
- ¿Los usuarios califican de forma diferente los juegos según plataforma?
- ¿Qué tan consistente es el desempeño de un título entre plataformas?
- ¿Cómo cambian las preferencias entre NA, EU y JP?
- ¿Cómo debería distribuirse el presupuesto de marketing?

---

# 🚀 18. Posibles extensiones

Como evolución del proyecto, podrían incorporarse modelos predictivos para estimar el potencial comercial de nuevos lanzamientos.

### Posibles líneas de trabajo

**Modelos de regresión**

```text
Ventas ~ Plataforma
       + Género
       + Critic Score
       + User Score
       + Año
       + Región
       + Rating
```

**Machine Learning**

- Random Forest.
- Gradient Boosting.
- XGBoost.
- LightGBM.

**Segmentación**

- Clustering de plataformas.
- Clustering de géneros.
- Segmentación de mercados regionales.

**Modelos predictivos**

Predicción de:

```text
High Sales
Medium Sales
Low Sales
```

También sería posible desarrollar un modelo de clasificación para identificar títulos con alta probabilidad de convertirse en **blockbusters**.

---

# 🎯 Conclusión

El análisis demuestra que el éxito comercial en la industria de videojuegos no depende de una única variable.

Los resultados sugieren una combinación de factores:

```text
Plataforma
    +
Género
    +
Calidad crítica
    +
Fuerza de franquicia
    +
Distribución multiplataforma
    +
Mercado regional
    +
Momento del ciclo tecnológico
```

La principal conclusión estratégica es que **la inversión publicitaria para 2017 debe ser diferenciada por región y etapa tecnológica**, en lugar de aplicar una estrategia global uniforme.

En Occidente, la oportunidad se concentra principalmente en **PS4 y Xbox One**, con especial atención a títulos de alto impacto en géneros como **Shooter, Action y Sports**.

En Japón, la estrategia debe orientarse hacia **Nintendo 3DS, PlayStation Vita y Role-Playing/JRPG**, reconociendo las particularidades estructurales del mercado.

Desde la perspectiva de Data Science, el proyecto demuestra la importancia de combinar:

> **calidad de datos + análisis exploratorio + estadística inferencial + segmentación + interpretación de negocio**

para convertir datos históricos en decisiones estratégicas.

---

## 👤 Autor

**Data Science Portfolio**

Proyecto desarrollado como ejercicio de análisis de datos, estadística aplicada y toma de decisiones basada en evidencia.

### Competencias demostradas

- Data Cleaning & Data Quality
- Exploratory Data Analysis
- Statistical Analysis
- Hypothesis Testing
- Correlation Analysis
- Market Segmentation
- Business Intelligence
- Data Visualization
- Python
- Pandas
- NumPy
- SciPy
- Seaborn
- Matplotlib
- Reproducible Data Analysis
- Business Storytelling
- Strategic Decision Making

---

## 📄 Licencia

Este proyecto se desarrolla con fines educativos y de portafolio profesional.

El dataset utilizado corresponde a la fuente proporcionada para el proyecto de análisis.
