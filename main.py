from typing import Union
from fastapi import FastAPI

#Creacion de aplicacion FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World%!'}