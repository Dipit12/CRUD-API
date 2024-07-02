from fastapi import FastAPI
app = FastAPI()

@app.get("/") # here get is the http method, / is the path/route
async def root(): # root is the function name
    return {"message":"Welcome to my API"}

@app.get ("/login")
async def login():
    return {"message":"Login Successful"}

