from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/") #if the path is same then the first function would be called
def home():
    return {"message":"This is the home page"}

@app.get("/posts")
def get_posts():
    return {"data":"These are your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)): # here payLoad is the variable storing the data, received from Body stored in a dict format
    print(payLoad)
    return {"new_post": f"title{payLoad['title']} content{payLoad['content']}"}
