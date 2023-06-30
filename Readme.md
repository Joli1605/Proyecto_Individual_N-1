

 _ _PROYECTO INDIVIDUAL Nº1_ _ 
 
Trabajo en el rol de un ***MLOps Engineer***.



 **'Descripción del Proyecto'**
El propósito de este proyecto es realizar la limpieza y preparación de datos relacionados con películas, así como desarrollar una API para facilitar la consulta de información. Esta plataforma permitirá a los usuarios obtener información detallada sobre películas y también acceder a un sistema de recomendación. 


## ** Proceso de limpieza y transformación.
Archivo= Limpieza_datos.ipynb

Antes de comenzar con el proceso de transformación y limpieza del conjunto de datos se procedio a cargar el Dataframe utilizando Pandas, luego se procedio a analizar las columnas. Se desanidaron aquellas columnas anidadas teniendo en cuenta las columnas importantes que luego se utilizaran para la API. Se crearon dataset y a medida fueron incorporadas las columnas ya desanidadas al dataframe original. Se procedio a rellenar la columna budget con ceros. Se eliminaron valores nulos y aquellas anomalías.Se procedio a crear un nueva columna con los valores de 'return', se creo la columna release_year en donde se extrajeron los años de la fecha de estreno. Además se procedió a eliminar aquellas columnas que no tenian algun significado importante para su posterior analisis. 
Al realizar la limpieza del dataframe movie_data creamos el csv Datalimpia.csv, ya con las columnas desanidas y la limpieza realizada.
En el caso del archivo credits.csv este tambien fueron desanidadas las columnas crew y cast. Luego se realizao una combinación de ambos dataframe y obtuvimos como resultado el archivo data_combined.csv.

## ** Desarrollo API.
Se encontrarán con funciones en las cuales se podran realizar consultas respectos a peliculas,actores y directores. Ademas podran consultar la cantidad de filmaciones en determinados meses y dias. 

+ def **cantidad_filmaciones_mes( *`Mes`* )**:
+ def **cantidad_filmaciones_dia( *`Dia`* )**:
+ def **score_titulo( *`titulo_de_la_filmación`* )**:
+ def **votos_titulo( *`titulo_de_la_filmación`* )**:
+ def **get_actor( *`nombre_actor`* )**:
+ def **get_director( *`nombre_director`* )**:


## ** Analísis exploratorios de datos._(Exploratory Data Analysis-EDA)_

Acá te encontrás con las relaciones que hay entre las variables de los datasets. Podras visualizar un resumen estadistico de las variables númericas,podras visualizar la dispercion entre las variables del dataframe budget y renveu, te encontraras con una nube de palabras con las palabras más frecuentes en los títulos de las películas







