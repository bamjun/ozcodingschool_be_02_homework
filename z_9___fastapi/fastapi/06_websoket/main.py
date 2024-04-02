from fastapi import FastAPI
from pathlib import Path
from fastapi.responses import HTMLResponse
from sockets import router as socket_router



app = FastAPI()
app.include_router(socket_router)

# socket -> ws


@app.get("/")
def index():
    index_html = Path('index.html').read_text()

    return HTMLResponse(content=index_html)


# uvicorn main:app --reload