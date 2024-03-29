from fastapi import FastAPI
from books import route as books_route
from sync_async_test import router as sync_async_test_router

app = FastAPI()
app.include_router(books_route)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
