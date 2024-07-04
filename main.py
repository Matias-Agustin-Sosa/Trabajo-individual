# Hacer la siguiente importación de la clase:
from fastapi import FastAPI
import pandas as pd
import ast
# Instanciar la aplicación: 
app = FastAPI()
# uvicorn main:app --reload (levanta la API)

@app.get('/Cantidad peliculas Mes') 
def cantidad_filmaciones_mes(mes: str):
    # Leemos el archivo
    df = pd.read_csv("Movies_dataset(ETL)_Final.csv")
    
    # Creamos un dicionario con meses para que caundo el usuario ingrese el mes sepamos su valor numerico
    diccionario = {"Enero": 1,"Febrero": 2,"Marzo": 3,"Abril": 4,"Mayo" :5,"Junio" :6,"Julio" :7,"Agosto" :8,"Septiembre" :9,"Octubre" :10,"Noviemre" :11,"Diciembre" :12,
                   "enero": 1,"febrero": 2,"marzo": 3,"abril": 4,"mayo" :5,"junio" :6,"julio" :7,"agosto" :8,"septiembre" :9,"octubre" :10,"noviemre" :11,"diciembre" :12
                   }
    
    # Revisamos si el mes ingresado es correcto
    if mes in diccionario:
        # Extraemos el mes de la columna release_date y creamos una columna mes con su valor numerico (.dt.month)
        df['mes'] = pd.to_datetime(df["release_date"]).dt.month
        # Creamos una mascara para filtrar por el mes buscado
        mes_return = df[df["mes"] == diccionario[mes]]
        
        # mes_return.shape[0]: contamos la cantidad de peliculas devueltas
        return f"Cantidad de peliculas estrenadas en el mes {mes}: {mes_return.shape[0]}"
    
    # Si el mes es incorrecto retornamos el siguiente mansaje
    else:
        return "Ingrese un mes valido: [Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviemre, Diciembre]"
    
@app.get("/Cantidad peliculas Dia")
def cantidad_filmaciones_dia(Dia: str):
    
    df = pd.read_csv("Movies_dataset(ETL)_Final.csv")

    # Creamos un dicionario con dias para que caundo el usuario ingrese el dia sepamos su valor texto (en ingles)
    dias = {"Lunes" : "Monday", "Martes": "Tuesday", "Miercoles": "Wednesday", "Jueves": "Thursday", "Viernes": "Friday", "Sabado": "Saturday", "Domingo": "Sunday",
            "lunes" : "Monday", "martes": "Tuesday", "miercoles": "Wednesday", "jueves": "Thursday", "viernes": "Friday", "sabado": "Saturday", "domingo": "Sunday"
            }

    # Revisamos si el dia ingresado es correcto
    if Dia in dias:
        # Extraemos el dia de la columna release_date, en ingles (dt.strftime("%A"))
        df["dia"] = pd.to_datetime(df["release_date"]).dt.strftime("%A")
        # Creamos una mascara para filtrar por el dia buscado
        dia_return = df[df["dia"] == dias[Dia]]
        
        # dia_return.shape[0]: contamos la cantidad de peliculas devueltas
        return f"Cantidad de peliculas estrenadas en el dia {Dia}: {dia_return.shape[0]}"
    
     # Si el dia es incorrecto retornamos el siguiente mansaje
    else:
        return "Ingrese un dia valido: Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo, lunes, martes, miercoles, jueves, viernes, sabado, domingo"

@app.get("/Titulo Pelicula Popularidad")
def score_titulo(titulo_de_la_filmación: str):
    
    df = pd.read_csv("Movies_dataset(ETL)_Final.csv")

    # Buscamos el titulo ingresado 
    for titulo in df["title"]:
        # Si existe
        if titulo_de_la_filmación == titulo:
            # Extraemos el año (.dt.year) de release_date y lo ponemos en una nueva columna año
            df['año'] = pd.to_datetime(df["release_date"]).dt.year
            # Creamos una mascara para filtrar por el titulo buscado
            titulo_return = df[df["title"] == titulo_de_la_filmación]
            
            # Retornamos el titulo, año y su popularidad
            return f"La pelicula {titulo_return['title'].to_string(index=False)}, fue estrenada en el año {titulo_return['año'].to_string(index=False)} con una popularidad de: {titulo_return['popularity'].to_string(index=False)}"
    
    # si no existe retornamos este mensaje
    return "¡El titulo no existe!"
    
@app.get("/Titulo Pelicula Votos")
def votos_titulo(titulo_de_la_filmación: str):

    df = pd.read_csv("Movies_dataset(ETL)_Final.csv")

    # Buscamos el titulo ingresado 
    for titulo in df["title"]:
        # Si existe
        if titulo_de_la_filmación == titulo:
            # Extraemos el año (.dt.year) de release_date y lo ponemos en una nueva columna año
            df['año'] = pd.to_datetime(df["release_date"]).dt.year
            # Creamos una mascara para filtrar por el titulo buscado
            titulo_return = df[df["title"] == titulo_de_la_filmación]
            
            # Vemos si la cantidad de votos es suficiente
            if float(titulo_return["vote_count"]) >= 2000:
                # Retornamos el titulo, año, votos y su promedio
                return f"La pelicula {titulo_return['title'].to_string(index=False)}, fue estrenada el año {titulo_return['año'].to_string(index=False)}.La misma cuenta con un total de {titulo_return['vote_count'].to_string(index=False)} votos, con un promedio de {titulo_return['vote_average'].to_string(index=False)}"

            # Si los votos son menores a 2000
            else:
                # Retornamos el titulo y año, ademas de un aviso de votos insuficioentes
                return f"La pelicula {titulo_return['title'].to_string(index=False)}, fue estrenada el año {titulo_return['año'].to_string(index=False)},¡La misma no cuenta con mas de 2000 votos!"

    # si no existe retornamos este mensaje
    return "¡El titulo no existe!"

@app.get("/Actor Retorno")
def get_actor(nombre_actor):
    # Si  se encuentra el nombre
    try:
        df = pd.read_csv("Movies_dataset(ETL)_Final.csv")
        df_c = pd.read_csv("Credits(ETL)_Final.csv")
        
        # Creamos una columna bool para ver si el actor esta en la pelicula usando la columna cast_name
        df_c["encontro"]= df_c["cast_name"].apply(lambda x: nombre_actor in x)
        encontro = df_c[df_c["encontro"] == True]

        # Lisata para guardar los id de las peliculas en donde esta el actor
        lista_peliculas = []

        # Insertamos los id en la lista
        for id in encontro["id"]:
            if id != None:
                lista_peliculas.append(id)
        
        # Creamos una variable para sumar los retornos
        total = 0
        # Busco las peliculas
        for id_p in lista_peliculas:
            filtro = df[df["id"] == id_p]
            # Sumo los retornos
            total += float(filtro["return"])

        # Retorno el nombre del actor, la cantidad de paliculas (len(lista_peliculas)), el total del retorno y su promedio
        return f"El actor {nombre_actor} ha participado en {len(lista_peliculas)} peliculas, el mismo a conseguido un retorno de {total} con un promedio de {total/int(len(lista_peliculas))}"

    # Si no se encuentra
    except:
        return "¡Nombre no valido!"

@app.get("/Director Retorno")
def get_director(nombre_director):

    df = pd.read_csv("Movies_dataset(ETL)_Final.csv")
    df_c = pd.read_csv("Credits(ETL)_Final.csv")
    
    # Busco el director
    df_c["encontro"]= df_c["crew_name"].apply(ast.literal_eval).apply(lambda x: nombre_director in x)
    encontro = df_c[df_c["encontro"] == True]

    # Lisata para guardar los id de las peliculas en donde esta el director
    lista_peliculas = []

    # Insertamos los id en la lista
    for id in encontro["id"]:
        if id != None:
            lista_peliculas.append(id)

    # Creamos una variable para sumar los retornos
    total = 0
    # Busco las peliculas
    for id_p in lista_peliculas:
        filtro = df[df["id"] == id_p]
        # Sumo los retornos
        total += float(filtro["return"])
    
    # Listado de peliculas
    df_filtrado = df[df['id'].isin(lista_peliculas)]
    

    return f"El actor {nombre_director} ha participado en {len(lista_peliculas)} peliculas, el mismo a conseguido un retorno de {total}", df_filtrado[["title","release_date","return","budget","revenue"]]



