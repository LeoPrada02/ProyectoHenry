# Proyecto individual Henry
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
