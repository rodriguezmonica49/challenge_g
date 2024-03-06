from typing import List, Union
from connection import engine
from fastapi import FastAPI
from cargar_employees import read_csv, clean_data
app = FastAPI()

from pydantic import BaseModel


class DataSerializer(BaseModel):
    filename: str
    nametable: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/load_data")
def load_data(data: DataSerializer):
    df_employees = read_csv(data.filename)
    df_employees = clean_data(df_employees)
    df_employees.to_sql(data.nametable, engine, chunksize=419,index=False, method='multi', if_exists='replace')

    return {"result": "Data cargada"}

