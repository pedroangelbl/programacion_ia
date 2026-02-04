from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/items/")
def list_items():
    pass

@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass
