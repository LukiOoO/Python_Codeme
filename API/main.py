from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional


app = FastAPI()
app.counter = 0

class HelloResp(BaseModel):
    msg: str

class Product(BaseModel):
    name : str
    desc: Optional[str] = None
    price: float
    code: str
    tax: Optional[float] = None



@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)

@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name.capitalize()}")

@app.post("/products/")
def create_product(prod: Product):
    # save to date
    return  prod