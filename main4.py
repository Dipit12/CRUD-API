# Every app has these 4 basic operations namely Create,Read,Update,Delete(CRUD)
"""
Create - POST
Read - GET
Update - PUT
Delete - DELETE
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Optional
app = FastAPI()
class Post(BaseModel):
    title:str
    content:str
    rating:Optional[int] = None

my_posts = [{"title":"title of post1","content":"content of post1","id":1},{"title":"favourite food","content":"i love butter chicken","id":2}]
@app.get("/")
def home_page():
    return {"message":"Home page"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post:Post):
    print(post)
    print(post.dict())
    my_posts.append(post.dict())
    return {"data":"new post"}


