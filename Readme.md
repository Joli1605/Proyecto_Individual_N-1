

 _ _PROYECTO INDIVIDUAL Nº1_ _ 
 
Trabajo en el rol de un ***MLOps Engineer***. 👩‍🔬



 **'Descripción del Proyecto'**
El propósito de este proyecto es realizar la limpieza y preparación de datos relacionados con películas, así como desarrollar una API para facilitar la consulta de información. Esta plataforma permitirá a los usuarios obtener información detallada sobre películas y también acceder a un sistema de recomendación. 
## Librerías utilizadas
- [python](https://www.python.org/): El lenguaje de programación principal utilizado en este proyecto.
- [uvicorn](https://www.uvicorn.org/): Un servidor ASGI de alto rendimiento.
- [FastAPI](https://fastapi.tiangolo.com/): Un marco web moderno y rápido para crear APIs con Python.
- [pandas](https://pandas.pydata.org/): Una biblioteca para el análisis y manipulación de datos.
- [scikit-learn](https://scikit-learn.org/): Una biblioteca de aprendizaje automático para Python.
- [datetime](https://docs.python.org/3/library/datetime.html): Una biblioteca para manipulación de fechas y tiempos en Python.
- [re](https://docs.python.org/3/library/re.html): Un módulo para operaciones de expresiones regulares en Python.

## ** Proceso de limpieza y transformación.(ETL-Extract, Transform, Load)
El proceso de ETL es una etapa fundamental en este proyecto, que consiste en extraer los datos de origen, transformarlos en un formato adecuado y cargarlos en una estructura final. En este caso, se aplicó el proceso de ETL a los datos relacionados con películas.

Para llevar a cabo el proceso de limpieza y transformación, se utilizó un archivo específico denominado "Limpieza_datos.ipynb". A continuación se describe brevemente el flujo de trabajo realizado en dicho archivo:
Extracción: Se cargaron los datos iniciales en un DataFrame utilizando la biblioteca Pandas.
Transformación: Se analizaron las columnas del DataFrame y se llevaron a cabo diversas tareas, como la desanidación de columnas anidadas, la creación de nuevos conjuntos de datos y la eliminación de columnas irrelevantes.
Limpieza: Se realizaron acciones para limpiar los datos, como el reemplazo de valores nulos, la eliminación de anomalías y la modificación de columnas para obtener información útil, como el cálculo del retorno de inversión y la extracción del año de estreno.
Almacenamiento: Una vez finalizada la limpieza y transformación, se guardó el DataFrame resultante en un archivo CSV denominado "Datalimpia.csv". Además, se combinaron los datos del archivo "credits.csv" después de aplicar un proceso similar de desanidación de columnas, y el resultado se guardó en el archivo "data_combined.csv".

## ** Desarrollo API.
Se encontrarán con funciones en las cuales se podran realizar consultas respectos a peliculas,actores y directores. Ademas podran consultar la cantidad de filmaciones en determinados meses y dias. Dispondran de un sistema de recomendación.
La API se encuentra en el siguiente enlace: [API Peliculas](https://proyecto-individual-ndeg1.onrender.com/docs#/)

💻 Las siguientes funciones se encuentran en main.py

+ def **cantidad_filmaciones_mes( *`Mes`* )**:devuelve la cantidad de filmaciones realizadas en el mes especificado.
+ def **cantidad_filmaciones_dia( *`Dia`* )**: devuelve la cantidad de filmaciones realizadas en el día especificado. 
+ def **score_titulo( *`titulo_de_la_filmación`* )**:devuelve el puntaje de la película con el título especificado y el año de estreno.
+ def **votos_titulo( *`titulo_de_la_filmación`* )**:devuelve la cantidad de votos recibidos por la película ,año de estreno y promedio.
+ def **get_actor( *`nombre_actor`* )**:devuelve información detallada sobre un actor específico.
+ def **get_director( *`nombre_director`* )**:devuelve información detallada sobre un director específico. 
+ def **Sistema_recomendacion( *`titulo`* )**:Implementa un sistema de recomendación de películas. Toma como entrada el título de una película y devuelve una lista de las 5 películas recomendadas basadas en la similitud de puntuación con la película ingresada.

Esta API está implementada en Python utilizando FastAPI y Uvicorn;
** 'Importamos las bibliotecas necesarias' **
from fastapi import FastAPI
import uvicorn

** 'Creamos una instancia de la aplicación FastAPI' **
app = FastAPI()

** 'Definimos rutas y funciones' **
... 

** 'Punto de entrada principal del programa' **
if __name__ == "__main__":
    # Inicia el servidor Uvicorn con la aplicación FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)



## ** Analísis exploratorios de datos._(Exploratory Data Analysis-EDA)_
Se pueden esperar los siguientes resultados clave al explorar los datos:

Resumen estadístico de variables numéricas: Al obtener el resumen estadístico de las variables numéricas, se pueden extraer medidas como la media, la mediana, la desviación estándar y los valores mínimo y máximo. Estos datos proporcionan una visión general de la distribución y la variabilidad de los datos numéricos, lo que puede ayudar a identificar posibles anomalías, valores atípicos o patrones interesantes en los datos.

Visualización de la dispersión entre variables "budget" y "revenue": Al visualizar la dispersión entre las variables "budget" (presupuesto) y "revenue" (ingresos), es posible analizar la relación entre estos dos atributos. Aca se encontrará con un gráfico de dispersión mostrando si existe una tendencia o patrón entre el presupuesto y los ingresos de las películas. 

Además de estos resultados clave, es posible realizar otros análisis exploratorios de datos según las características específicas del conjunto de datos de películas  Estos análisis incluyen visualizaciones de palabras clave más frecuentes en los títulos de las películas,a travez del grafico nube de palabras, identificación de outliers o anomalías en la columna "popularity", y análisis de la correlación entre variables como "vote_average" y "popularity".











