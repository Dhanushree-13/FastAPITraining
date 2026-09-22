#HTTP Methods:Are a way to talk (From browser) to the server
#methods 
#GET : Read data
#POST:create a new data
#PUT : Replace existing data
#PATCH : Partial update
#DELETE : Remove data
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def home():
    return{"page":"Home"} 

@app.get("/about")
def about():
     return{"page":"About","author":"Dhanu"}

@app.get("/health")
def health():
     return {"Status":"ok"}

#POST request
@app.post("/create")
def create_something():
     return {"message":"Created"}
#Path parameters
@app.get("/student/{roll}")
def get_result(roll):
     return {"Result":"Distinction","roll":roll}
#Path Parameters with type hint
@app.get("/candidate/{roll}")
def get_Candidate(roll:int):
     return {"Result":"Distinction","roll":roll,"type":str(type(roll))}

#Pydantic model
class Item(BaseModel):
     name:str
     price:float
     in_stock:bool=True

@app.post("/items")
def create_item(item:Item):
     return {"received":item,"total_price":item.price*1.18}