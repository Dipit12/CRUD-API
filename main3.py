# working with pydantic
from fastapi import FastAPI
from fastapi.params import Body
from fastapi.params import Optional
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/") #if the path is same then the first function would be called
def home():
    return {"message":"This is the home page"}

@app.get("/posts")
def get_posts():
    return {"data":"These are your posts"}

@app.post("/createposts")
def create_posts(new_post:Post): # here new_post is the variable storing Post pydantic model, it would check if the title and content are of string type
    print(new_post)
    print(new_post.dict())
    return {"data":"new post"}
# title string, content string