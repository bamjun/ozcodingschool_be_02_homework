from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
