# PROYECTO INDIVIDUAL Nº1

## Introdución:
Para este proyecto se pidió crear una API, utilizando la libreria FastApi, y dos sets de datos, uno con peliculas (Movies) y otro con su respectivo reparto (Credits). La API debía contar con seis funciones, que se explicaran a detalle más abajo, y una función de recomendación que utilice Machine Learning. Previemente, se realizó una limpieza de los datos (ETL) y luego un análisis de los mismos (EDA) para el modelo de Machine Learning.

## ETL
[![Captura-de-pantalla-35.png](https://i.postimg.cc/yxfvgFtY/Captura-de-pantalla-35.png)](https://postimg.cc/BPKxR1Jd)

Se recibieron dos datasets (Movies y Credits), a estos se le aplicaron las siguientes transformaciones:

#### Movies dataset
- Se rellenaron los valores nulos con 0 en las columnas **`revenue`** y **`budget`**.

- Se eliminaron los campos nulos de **`release_date`**.

- Se cambió el tipo de dato a fecha (AAAA-mm-dd) en la columna **`release_year`**.

- Se creó una nueva columna llamada  **`return`** que proviene de la división de **`revenue`** y **`budget`**.

- Se eliminaron las columnas innecesarias:  **`video`**, **`imdb_id`**,  **`adult`**, **`original_title`**, **`poster_path`**, **`homepage`**, **`overview`**, **`status`**, **`tagline`** y **`Unnamed: 0`**.

- También se desanidaron las columnas **`genres`**, **`production_companies`**, **`spoken_languages_iso`** y **`belongs_to_collection`**, extrayendo solo la información de interés de cada una.

- Al momento de crear el nuevo dataset con los cambios hechos, solo me quedé con 20000 registros por temas de espacio de **almacenamiento** y **procesamiento** en render.

#### Credits dataset
- Se extrajeron las columnas anidadas denrto de las columnas **`cast`** y  **`crew`**. Se obtuvieron las siguientes columnas: **`cast_character`**, **`cast_name`**, **` crew_department`**, **`crew_job`** y **`crew_name`** (eran más columnas pero fueron eliminadas por tener información irrelevante para este proyecto).

- Se realizó un chequeo de filas duplicadas.

- Al momento de crear el nuevo dataset con los cambios hechos, solo me quedé con 20000 registros por temas de espacio de **almacenamiento** y **procesamiento** en render.

## EDA
[![Captura-de-pantalla-36.png](https://i.postimg.cc/R0Np7BqL/Captura-de-pantalla-36.png)](https://postimg.cc/LqFVSGtJ)

Para saber un poco más de los datos y su comportamiento se procedió a crear un EDA, en él se analizó los dos dataset:

	1.Se buscaron nulos en las columnas.
	2.Se buscaron valores faltantes.
	3.Se chequeó filas duplicadas.
	4.Se revisó el tipo de dato de cada columna.
	5.Se realizaron gráficos con columnas como cantidad de votos, popularidad y retorno.
	6.Por último se creo una nube de palabras para ver la frecuencia de las mismas.

## Fast API
[![Captura-de-pantalla-37.png](https://i.postimg.cc/PrvbhQNK/Captura-de-pantalla-37.png)](https://postimg.cc/Vd10WMqb)

En la API creada se le incluyeron siete funciones:
- La primera llamada **cantidad_filmaciones_mes**, se le entrega un mes en español y devuelve la cantidad de películas hechas en ese mes.

- La segunda llamada **cantidad_filmaciones_dia**, se le entrega un día en español y devuelve la cantidad de películas hechas en ese día.

- La tercera llamda **score_titulo**, se ingresa un título de película y devuelve el mismo con su año de estreno y su popularidad.

- La cuarta llamada **votos_titulo**, se ingresa un título de película y devuelve el mismo con el año de estreno, la cantidad de votos y su promedio. En caso de que los votos sean menores a 2000, devuelve un mensaje que dice que la cantidad de votos es insuficioente.

- La quinta llamada **get_actor**, se ingresa el nombre del actor y se devuelve su nombre, la cantidad de película en las que participó, su retorno y un promedio del retorno.

- La sexta llamada **get_director**, se ingresa el nombre del director y se devuelve su nombre, el retorno del mismo y las película en las que participó, a demás de los datos de cada una.

- La septima llamada **recomendacion**, se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

Para finalizar, la API se cargó en render en modo público. Cabe aclarar que para la función de recomendación se creó un dataset especial con solo 5000 registros y las tres columnas necesarias (título, votos y género) debido a que render brinda una capacidad de procesamiento limitada muy chica para modelos de Machine Learning. 
