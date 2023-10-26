# Proyecto individual Henry
!(Alt text)[https://gearmoose.com/wp-content/uploads/2017/04/best-movies-for-men.jpg]

## Link API:
https://proyecto-henry-ctb7.onrender.com/docs

## Contexto
  En este proyecto se simula un entorno laboral en el cual nuestra tarea es disponibilizar una api con funciones especificas para obtener informacion valiosa, todo esto a partir de unos archivos csv los cuales vienen sucios, asi que tendremos que limpiar estos datasets en un proceso de ETL, luego explorar las variables y las columnas en un proceso de EDA, y finalmente con la ayuda de la libreria Fastapi y render disponibilizaremos un servicio web para el consumo de la informacion extraída.

## Orden cronologico
## Parte 1: ETL
### Orden de archivos: primero-> creditos-> funciones api
  Primero empezamos con el ETL (Archivo del mismo nombre), en el cual hacemos los cambios pertinentes para una mejor extraccion de los datos, esto significa principalmente desanidar las columnas necesarias para poder crear las columnas solicitadas, luego de terminar con el dataset de movies continuamos con el dataset de crew, y una vez terminamos con crew juntamos los datasets con merge y el resultado de este merge sera el dataframe que usaremos para las funciones

## Parte 2: Funciones API
  Con el dataset listo hacemos las siguiente funciones para extraer la informacion requerida:
  
->def peliculas_idioma: Recibe un idioma (en, es, fr, etc..) y devuelve la cantidad de peliculas hechas en ese idioma

->def peliculas_duracion: Esta funcion recibe el nombre de una pelicula y devuelve la duracion y el año de salida de la pelicula

->def franquicia: Esta funcion recibe la franquicia de una pelicula  y devuelve la cantidad de peliculas de esa franquicia, la ganancia y la ganancia promedio

->def peliculas_pais: Esta funcion recibe un pais y devuelve la cantidad de peliculas hechas en ese pais

->def productoras_exitosas: Esta funcion recibe una productora y devuelve cuantas peliculas a realizado esa productora junto a la ganancia total

->def get_director: Esta funcion recibe el nombre de un director y devuelve todas las peliculas hechas por él junto a los datos de las peliculas de manera individual en una lista

->def recomendacion: Esta funcion recibe el nombre de una pelicula y devuelve las 5 mas 'similares' (no logre usar todo el dataset por el alto coste computacional asi que la matriz esta recortada a las 1000 peliculas mas populares)

Todas estas funciones se encuentran en main.py

## Parte 3: EDA
En este EDA exploramos las relaciones entre algunas variables y la evolucion y crecimiento del cine con el paso de los años, asi como ver cuales son las productoras mas importantes del cine, el proceso completo se encuentra en el archivo EDA.ipynb

## Parte 4: Modelo de recomendacion
El proceso en el que creo la matriz de recomendacion que luego uso se puede ver en Algoritmo Recomendacion.ipynb, la creo en ese notebook, luego la exporto como csv y en main.py la vuelvo a importar y la transformo en un array, de esta manera la matriz no es creada en la API haciendo que sea menos pesada y por consiguiente mas rapida, tambien para ahorrarme problemas de espacio con el render, para ver mas a detalle el proceso y la explicacion de la matriz les refiero el video con el que me guié

[Modelo Tdfid](https://www.youtube.com/watch?v=ijtxuF_5kEU&ab_channel=AISciences).<br>

## Video

[Video Aqui](https://drive.google.com/file/d/167J2tuHOYIdFUTo7pAQub6qPrRYhf2rW/view?usp=drive_link)






