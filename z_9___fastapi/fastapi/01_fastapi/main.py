from fastapi import FastAPI
from items import router as items_router
from users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='DEBUG', reload=True)
