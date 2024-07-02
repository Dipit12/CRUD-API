
from fastapi import FastAPI,Response,HTTPException,status,Depends
from pydantic import BaseModel
from fastapi.params import Optional
from random import randrange
import psycopg2
from . import models
from sqlalchemy.orm import Session
from .database import engine,SessionLocal

models.Base.metadata.create_all(bind = engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Post(BaseModel):
    title:str
    content:str
    published: bool = True

my_posts = [{"title":"title of post1","content":"content of post1","id":1},{"title":"favourite food","content":"i love butter chicken","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    
def find_index(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def home_page():
    return {"message":"Home page"}

@app.get("/sqlalcheny")
def test_posts(db: Session = Depends(get_db)):
    return {"status":"success"}
    

# to get a all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# to create a new post
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
# to get the latest post
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[-1]
    return {"data":post}

# to get a specific post
@app.get("/posts/{id}") #here id is the path parameter
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
        #response.status_code = 404
        #return {"message":f"Post with id {id} not found"}
    return{"post_detail":post}

# to delete a post
@app.delete("/posts/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index(id)
    if index == None:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} doesnot exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# to update a post
@app.put("/posts/{id}")
def update_post(id:int,post: Post):
    index = find_index(id)
    if index == None:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} doesnot exist")
    
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data":post_dict}