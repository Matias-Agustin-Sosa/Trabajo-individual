# PROYECTO INDIVIDUAL Nº1

## Introdución:
Para este proyecto se pidio crear una API, utilizando la libreria FastApi, y dos sets de datos uno con peliculas (Movies) y otro con su respectivo reparto (Credits). La API devia contar con seis funciones, que se explicaran a detalle mas abajo, y una funcion de recomandacion que utilize Machine Learning. Antes de esto, se devio hacer una limpieza de los datos (ETL) y luego un analicis de los mismos (EDA) para el modelo de Machine Learning.

## ETL
[![Captura-de-pantalla-35.png](https://i.postimg.cc/yxfvgFtY/Captura-de-pantalla-35.png)](https://postimg.cc/BPKxR1Jd)

Se recibieron dos datasets Movies y Credits, a estos se le aplicaron las siguientes transformaciones:

#### Movies dataset
- Se relleno los valores nulos con 0 en las columnas **`revenue`** y **`budget`**.

- Se eliminaron los campos nulos de **`release_date`**.

- Se cambio el tipo de dato a fecha (AAAA-mm-dd) en la columna **`release_year`**.

- Se creo una nueva columna llamada  **`return`** que proviene de la divicion de **`revenue`** y **`budget`**.

- Se elimino las columnas inecesarias:  **`video`**, **`imdb_id`**,  **`adult`**, **`original_title`**, **`poster_path`**, **`homepage`**, **`overview`**, **`status`**, **`tagline`** y **`Unnamed: 0`**.

- Tambien se desanidaron las columnas **`genres`**, **`production_companies`**, **`spoken_languages_iso`** y **`belongs_to_collection`**, extrallendo solo la informacion de interes en para cada una.

- Al momento de crear el nuevo dataset con los cambios echos, solo me quede con 20000 registros por temas de espacio de **almacenamiento** y **procesamiento** en render.

#### Credits dataset
- Se extrajeron las columnas anidadas denrto de las columnas **`cast`** y  **`crew`**. Se obtuvieron las siguientes columnas: **`cast_character`**, **`cast_name`**, **` crew_department`**, **`crew_job`** y **`crew_name`** (eran mas columnas pero fueron eliminadas por tener informacion irelevante para este proyecto).

- Se relizo un chequeo de filas duplicadas.

- Al momento de crear el nuevo dataset con los cambios echos, solo me quede con 20000 registros por temas de espacio de **almacenamiento** y **procesamiento** en render.

## EDA
[![Captura-de-pantalla-36.png](https://i.postimg.cc/R0Np7BqL/Captura-de-pantalla-36.png)](https://postimg.cc/LqFVSGtJ)

Para saver un poco mas de los datos y su comportamiento se procedio a crear un EDA, en el se analizo los dos dataset:

	1.Se buscaron nulos en las columnas.
	2.Se buscaron valores faltantes.
	3.Se chequeo filas duplicadas.
	4.Se reviso el tipo de dato de cada columna.
	5.Se realizaron graficos con columnas como cantidad de votos, popularidad y retorno.
	6.Por ultimo se creo una nube de palabras para ver la frecuencia de las mismas.

## Fast API
[![Captura-de-pantalla-37.png](https://i.postimg.cc/PrvbhQNK/Captura-de-pantalla-37.png)](https://postimg.cc/Vd10WMqb)
En la API creada se le incluyeron ciete funciones:
- La primera llamada **cantidad_filmaciones_mes**, se le entrega un mes en español y devuelve la cantidad de peliculas echas en ese mes.

- La segunda llamada **cantidad_filmaciones_dia**, se le entrega un día en español y devuelve la cantidad de peliculas echas en ese día.

- La tercera llamda **score_titulo**, se ingresa un titulo de pelicula y devuelve el mismo con su año de estreno y su popularidad.

- La cuarte llamada **votos_titulo**, se ingresa un titulo de pelicula y devuelve el mismo con el año de estreno, la cantidad de votos y su promedio, en caso de que los votos no sean mas de 2000 el mensaje no devuelve los botos, si no un mensaje que dice que la cantidad de votos es insuficiente.

- La quinta llamada **get_actor**, se ingresa el nombre del actor y se devuelve su nombre, la cantidad de peliculas en las que participo, su retorno y un promedio del retorno.

- La secsta llamad **get_director**, se ingresa el nombre del director y se devuelve su nombre, el retorno del mismo y las peliculas en las que participo demas de los datos de cada una.

- La septima llamada **recomendacion**, se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

Para finalizar la API se cargo en render en modo publico, cabe aclarar que para la función de recomendacion se creo un dataset especial con solo 5000 registros y las tres columnas necesarias (titulo, votos y genero) devido a que render brinda una capacidad de procesamiento limitada muy chica para modelos de Machine Learning. 
