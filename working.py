from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return {"About": "Data"}

@app.get("/contact")
def contact():
    return {"message": "Contact page"}
    