from fastapi import FastAPI
from books import route as books_route

app = FastAPI()
app.include_router(books_route)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
