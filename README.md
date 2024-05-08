# HernyP1
# SteamGames
Trabajo realizado como "Proyecto Individual 1" para Bootcamp Henry - Data PT 08 -  Mayo 2024


Se realizó un proyecto que consiste en realizar un MVP sobre una base de datos correspondiente a juegos: Steam Games.
Los datos son recibidos en formato zip. 

ETL:
Para poder trabajar con los datos se realizó un ETL, realizando todas las transformaciones posibles, para lograr trabajar con datos limpios y legibles.
En el mismo se tuvieron en cuenta lo aprendido durante el curso.
Se analizaron los datos desanidando los datos primero, para lograr poder ver los mismos. 
A partir de ahí, se eliminaron nulos, duplicados, columnas que estaban de más. De esta forma se logró trabajar con datos de forma mas prolija y legible, logrando disminuir los tiempos.
Se realizaron ademas, cambios en nombres de columnas para evitar confusiones, y se reemplazo la fecha por el año correspondiente en cada caso, dado que es la información que yo necesito para poder realizar las funciones.
Una vez realizado este proceso, re prosiguió a guardar los mismos en parquet, para poder guardar los datos limpios.
Dado que hay que optimizar la memoria para que pueda correr mejor, se utilizó formato parquet para que los datos se compriman y ocupen menos memoria. Además, se consideró el 25 % de los datos de forma aleatoria, dado que es un MVP y no es necesario utilizar todos los datos.
Se realizó un ETL por cada archivo en archivos diferentes.
Los mismos tienen el nombre de "games", "items" y "reviews",

FEATURE ENGINEERING:
Se realizó un análisis de sentimientos con NLP, mediante una librería que se llama nltk.
Se realizó la clasificación utilizando el objeto de SentimentIntensityAnalyzer().
En los resultados obtenidos a partir de las palabras analizadas, se toma la columna de compound  que va a asignar un resumen general de la puntuación

