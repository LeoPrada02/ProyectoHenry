from fastapi import FastAPI
import pandas as pd

df= pd.read_csv('../New Folder (2)/df_directores.csv')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

'''
esta funcion recibe el diminutivo del idioma (en, es, fr...) y devuelve la cantidad de peliculas
hechas en ese idioma
'''

@app.get('/{idioma}')
def peliculas_idioma(idioma:str):
    contador= 0
    for i in df['original_language']:
        if idioma == i:
            contador+=1
        else:
            continue
    return contador

'''
Esta funcion recibe el nombre de una pelicula y devuelve la duracion y el año de salida de la pelicula
'''

@app.get('/duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    for i, j in enumerate(df['title']):
        if j == pelicula:
            return f"Duracion: {df['runtime'][i]} minutos, año: {df['release_year'][i]}"
        else:
            continue

'''
esta funcion recibe la franquicia de una pelicula  y devuelve la cantidad de peliculas de esa franquicia, la ganancia y la
ganancia promedio
'''

@app.get('/coleccion/{coleccion}')
def franquicia(Franquicia:str):
    collection = df[df['belongs_to_collection'] == Franquicia]
    numero = len(collection) 
    ganancia = collection['revenue'].sum()
    avg = collection['revenue'].mean()
    return f'La franquicia {Franquicia} tiene {numero} peliculas, una ganancia de {ganancia} y una ganancia promedio de {avg}'

'''
esta funcion recibe un pais y devuelve la cantidad de peliculas hechas en ese pais
'''

@app.get('/produccion_pais/{pais}')
def peliculas_pais(pais:str):
    paiss = df[df['country'] == pais]
    paiss['country']
    return f'se produjeron {paiss.shape[0]} en el pais {pais}'

'''
esta funcion recibe una productora y devuelve cuantas peliculas a realizado esa productora junto a la ganancia total
'''

@app.get('/productoras/{productora}')
def productoras_exitosas(productora:str):
    pr= df[df['prcompany1'] == productora]
    ganancia = pr['revenue'].sum()
    return (f'la productora {productora} tiene {len(pr)} peliculas y una ganancia total de {ganancia}')

'''
esta funcion recibe el nombre de un director y devuelve todas las peliculas hechas por él junto a los datos de las peliculas
de manera individual en una lista
'''

@app.get('/director/{director}')
def get_director(nombre_director):
    series = df[df['director'] == nombre_director]
    retorno = series['return'].sum()
    peliculas = []
                
    for i in range(len(series)):
        peli = {}
        peli['titulo'] = ((series['title'].iloc[i]))
        peli['fecha de estreno'] = (series['release_date'].iloc[i])
        peli['retorno'] = (series['return'].iloc[i])
        peli['presupuesto'] = (series['budget'].iloc[i])
        peli['ganancia'] = (series['revenue'].iloc[i])
       
        peliculas.append(peli)
    return (f'datos del director {nombre_director}: exito: {retorno}, peliculas: {peliculas}')
        