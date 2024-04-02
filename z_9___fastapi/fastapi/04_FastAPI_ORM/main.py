from fastapi import FastAPI
from routes.users import router as users_router
from routes.items import router as item_router

app = FastAPI()

# app.include_router(users_router)
# app.include_router(item_router)
app.include_router(users_router, prefix='/api/v1/users', tags=['User'])
app.include_router(item_router, prefix='/api/v1/items', tags=['Item'])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)