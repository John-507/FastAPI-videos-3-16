from typing import Union
from fastapi import FastAPI
from models.item_model import item 


#Creacion de aplicacion FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World%!'}

#get con nuevas rutas(Paths) y consulta(Query)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/calc")
def calcular(operando_1:float, operando_2:float):
    return{"suma":operando_1 + operando_2}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.price}

