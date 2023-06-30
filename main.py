from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn
from datetime import datetime
import re
from sklearn.neighbors import NearestNeighbors


# Cargar datos desde el archivo CSV y convertirlos a un dataframe

df_peliculas=pd.read_csv('./Data/DataLimpia.csv')
df_cast=pd.read_csv('./DataSets/cast.csv')
df_data_combined=pd.read_csv('./Data/data_combined.csv')



app = FastAPI()


@app.get("/cantidad_filmaciones_mes")
async def cantidad_filmaciones_mes(mes):
    mes = mes.lower()   #se convierte el parámetro mes a minúsculas utilizando el método lower()
    #se define un diccionario month_map que mapea los nombres de los meses en español a su número correspondiente. 
    month_map = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}
#Si no está presente, se retorna un mensaje indicando que el mes es inválido
    if mes not in month_map:
        return  f"Mes inválido: {mes}"
    #iterar sobre las fechas de estreno y obtener el total de las filmaciones.
    #Verifica si el mes de cada fecha coincide con el número del mes obtenido del diccionario month_map. 
    #Por cada coincidencia, se agrega 1 al total de filmaciones.
    cantidad = sum(1 for fecha in df_peliculas['release_date'] if datetime.strptime(fecha, '%Y-%m-%d').month == month_map[mes])
    return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"

@app.get("/cantidad_filmaciones_dia")
async def cantidad_filmaciones_dia(dia):
    dia = dia.lower() #Se convierte el parámetro mes a minúsculas utilizando el método lower()
    #Se define un diccionario dias_semana que mapea los nombres de las semanas en español a su número correspondiente
    #colocamos miercoles y sabado con y sin acentos.
    dias_semana = {
        'lunes': 0, 'martes': 1, 'miércoles': 2, 'miercoles' : 2, 'jueves': 3, 'viernes': 4, 'sábado': 5, 'sabado' : 5, 'domingo': 6
    }
    #sino se encuentra return
    if dia not in dias_semana:
        return  f"Día inválido: {dia}"
    # re.match() para encontrar coincidencias con el patrón de fecha.
    #creamos una lista fecha_formato_correcto
    fecha_formato_correcto = [fecha for fecha in df_peliculas['release_date'] if re.match(r'\d{4}-\d{2}-\d{2}', fecha)]
    # iterar sobre las fechas válidas en fecha_formato_correcto.
    #Se verifica si el día de la semana de cada fecha coincide con el número del día obtenido del diccionario dias_semana.
    #Por cada coincidencia, se agrega 1 al total de filmaciones.
    cantidad = sum(1 for fecha in fecha_formato_correcto if datetime.strptime(fecha, '%Y-%m-%d').weekday() == dias_semana[dia])
    
    return {'cantidad': f"{cantidad} 'de peliculas fueron estrenadas'",
            'mes': {mes}}


@app.get("/score_titulo")
async def score_titulo(titulo_de_la_filmacion):
    # Realiza la búsqueda de películas que coincidan con la primera palabra del título
    #El método str.split().str[0] para dividir el título en palabras y seleccionar la primera palabra, 
    #y luego se compara en minúsculas con titulo_de_la_filmacion.lower() 
    pelicula = df_peliculas[df_peliculas['title'].str.split().str[0].str.lower() == titulo_de_la_filmacion.lower()]
    
    #para encontrar películas cuyo título contenga titulo_de_la_filmacion en minúscula
    if pelicula.empty:
        pelicula = df_peliculas[df_peliculas['title'].str.lower().str.contains(titulo_de_la_filmacion.lower())]
    #empty. Si está vacío
    if pelicula.empty:
        return "No se encontraron películas en la base de datos con la palabra clave ingresada."
    #Si se encontró una película en alguno de los pasos anteriores, se extraen los datos relevantes de la primera fila de pelicula. 
    titulo = pelicula['title'].iloc[0] #se obtiene el título de la película.
    año = str(pelicula['release_year'].iloc[0])#se obtiene el año de lanzamiento y se convierte a cadena de caracteres.
    score = pelicula['vote_average'].iloc[0] #se obtiene el puntaje de la película.
    return f"La película {titulo} fue lanzada en el año {año} y tiene un puntaje de {score}"
    


@app.get("/votos_titulo")
async def votos_titulo(titulo_de_la_filmacion):
    #Encontrar películas cuyo primer palabra del título coincida con titulo_de_la_filmacion en minúsculas.
    pelicula = df_peliculas[df_peliculas['title'].str.split().str[0].str.lower() == titulo_de_la_filmacion.lower()]
    # encontrar películas cuyo título contenga titulo_de_la_filmacion en minúscula
    if pelicula.empty:
        pelicula = df_peliculas[df_peliculas['title'].str.lower().str.contains(titulo_de_la_filmacion.lower())]
    # No se encontraron películas con la palabra clave
    if pelicula.empty:
        
        return "No se encontraron películas en la base de datos con la palabra clave ingresada."
    
    # Obtener la cantidad de votos y el valor promedio de las votaciones
    cantidad_votos = pelicula['vote_count'].iloc[0] # se obtiene la cantidad de votos de la película. 
    promedio_votos = pelicula['vote_average'].iloc[0] # se obtiene el valor promedio de las votaciones de la película
    año = str(pelicula['release_year'].iloc[0]) #se obtiene el año de lanzamiento y se convierte a cadena de caracteres.
    #Si no cuenta con al menos 2000 valoraciones.
    if cantidad_votos < 2000:
        return f"La película {pelicula['title'].iloc[0]} no cumple con la condición de tener al menos 2000 valoraciones."

    mensaje = f"La película {pelicula['title'].iloc[0]} fue estrenada en el año {año}."
    mensaje += f" La misma cuenta con un total de {cantidad_votos} valoraciones"
    mensaje += f" y tiene un promedio de {promedio_votos}."

    return mensaje

@app.get("/get_actor")
def get_actor(nombre_actor):
    movie_count = 0
    movie_return = 0
    # buscamos el valor ingresado y dividimos el nombre en palabras y seleccionamos la primera palabra,luego se compara con nombre_actor.lower()
    actor_data = df_cast[df_cast['cast_name'].str.split().str[0].str.lower() == nombre_actor.lower()]

    #encontrar películas cuyo título contenga nombre_actor en minúscula
    if actor_data.empty:
        actor_data= df_cast[df_cast['cast_name'].str.lower().str.contains(nombre_actor.lower())]
    # No se encontraron actores con la palabra clave
    if actor_data.empty:
        return f"No se encontraron actores en la base de datos con la palabra clave {nombre_actor} ingresada."

    # Si se encontró un actor
    id_actor = int(actor_data['id_actors'].iloc[0]) #se obtiene el ID del actor y se convierte a entero
    name_actor = actor_data['cast_name'].iloc[0] #se obtiene el nombre del actor.

    #Iteramos el otro dataframe

    for index ,row in df_data_combined.iterrows():
        list_id_actors = row['id_actors'].strip('[]').split(',') #se obtiene la lista de IDs de actores, dividimos a lista se obtiene eliminando los corchetes ([]) alrededor de los IDs y dividiendo los IDs por comas (,) utilizando los métodos.
        list_id_actors = [int(i) for i in list_id_actors] 
        if id_actor in list_id_actors: #verificamos si el ID del actor buscado está presente en la lista de IDs de actores
            movie_count += 1 #se incrementa el contador de películas
            movie_return += row['return']  #sumamos los valores de return encontrados por el id actor

    promedio_retorno = movie_return / movie_count if movie_count > 0 else 0  #se calcula el promedio de retorno dividiendo movie_return/ movie_count siempre que movie_count sea mayor a cero, sino se asigna 0.
    
    return f"El actor {name_actor} ha participado en {movie_count} películas, ha conseguido un retorno de {round(movie_return, 2)} con un promedio de {round(promedio_retorno, 2)} por filmación."



@app.get("/get_director")
def get_director(nombre_director):
    #lista vacía que almacenará las películas del director.
    movies_list = []
    #almacenar el valor total de retorno de las películas del director
    movie_return = 0
    #almacenar el nombre del director.
    name_director = ""
    #Se inicia un bucle for que itera sobre el DataFrame df_data_combined utilizando la función enumerate para obtener tanto el índice como el valor de la columna 'credit_job'.
    for index, valor in enumerate(df_data_combined['credit_job']):
            valor= eval(valor)#Esto convierte el valor de la columna en una lista de trabajos
    #se itera sobre la lista de job (valor) utilizando la función enumerate para obtener tanto el índice como el valor.
            for indexJob, job in enumerate(valor):
                if job == "Director": #"si es job igual a Director 
                    #encontramos registros cuyo primer palabra del nombre de actor coincida con nombre_actor en minúsculas. 
                    director_name = eval(df_data_combined['credit_name'].iloc[index])[indexJob].lower()
                    if director_name == nombre_director.lower(): #Se verifica si el director_name obtenido coincide con el nombre_director. 
                        name_director = director_name #se actualiza la variable name_director
                        movie_return += df_data_combined['return'].iloc[index] #se suma el valor de retorno de la película actual 
                        #se agrega un diccionario con información de la película actual a la lista
                        movies_list.append({
                            "title": df_data_combined['title'].iloc[index],
                            "release_date": pd.to_datetime(df_data_combined['release_date'].iloc[index]).strftime('%Y-%m-%d'),
                            "return": df_data_combined['return'].iloc[index],
                            "budget": df_data_combined['budget'].iloc[index],
                            "revenue": df_data_combined['revenue'].iloc[index],
                        })
    #si no se encontró ningún director con el nombre ingresado returna lo siguiente.
    if name_director == "":
         return f"El nombre {nombre_director} ingresado no es valido, recuerde ingresar nombre y apellido"                
    
    return {
        "name_director": name_director,
        "movies_return": movie_return,
        "movies_list": movies_list 
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)


@app.get("/Sistema_recomendación")
def sistema_recomendacion (titulo_peli):
#Obtenemos la matriz de características de las películas a partir de la columna de popularidad del DataFrame
    X=df_peliculas[['popularity']].values
#Instanciamos un objeto de la clase KNeighborsClassifier
#Metrica ecludiana:utilizada para calcular la similitud entre dos puntos en un espacio multidimensional.
    clf= NearestNeighbors(n_neighbors=6,metric='euclidean')
# Entrenamos
    clf.fit(X)
#Convertimos el título de la película ingresada a minúsculas
    titulo_peli = titulo_peli.lower()
#buscamos el indice de la pelicula ingresada.
    peli_index = df_peliculas[df_peliculas['title'].str.lower()== titulo_peli]
    if peli_index.empty: 
        peli_index= df_peliculas[df_peliculas['title'].str.lower().str.contains(titulo_peli)]
    if peli_index.empty:
        return f'No existe {titulo_peli}  en esta base de datos'
    peli_index = peli_index.index[0]
    
#encontramos los indices de las peliculas que mas similares a la pelicula ingresada.
    _, indices_peli_similares = clf.kneighbors(X[[peli_index]])
#excluimos la pelicula ingresada
    indices_peli_similares= indices_peli_similares.flatten()[1:]

#Obtenemos los títulos y puntajes de las películas más similares
    recommended_movies = [(df_peliculas.loc[index, 'title'], df_peliculas.loc[index, 'popularity']) for index in indices_peli_similares]

#Ordenamos los títulos según el puntaje de similitud en forma descendente
    recommended_movies = sorted(recommended_movies, key=lambda x: x[1], reverse=True)

#Obtenemos solo los títulos de las películas ordenadas
    recommended_movies = [movie[0] for movie in recommended_movies]

    return recommended_movies


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
