from fastapi import FastAPI
from routes.users import router as users_router

app = FastAPI()

app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)