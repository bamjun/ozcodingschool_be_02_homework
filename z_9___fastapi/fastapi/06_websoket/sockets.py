# websocket 연결 -> ws://127.0.0.1:8000/ws
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from models import Message
from connection import manager
from dependencies import get_username

router = APIRouter()

@router.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    username = get_username(token)
    await manager.connect(websocket)


    while True:
        data = await websocket.receive_text()
        message = Message(username=username, text=data)
        await manager.broadcast(message.json())

