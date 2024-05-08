from fastapi import FastAPI
app = FastAPI()


import pandas as pd

#Importo los archivos
games=pd.read_csv("Archivos_MVP/games_mvp.csv",encoding="latin-1")
reviews= pd.read_parquet("Archivos_MVP/reviews_mvp.parquet")
items=pd.read_parquet("Archivos_MVP/item_mvp.parquet")

@app.get("/")
async def ruta_prueba():
    return "BOCA"