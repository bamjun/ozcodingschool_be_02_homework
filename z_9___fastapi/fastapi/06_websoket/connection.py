# websocket 연결 -> ws://127.0.0.1:800

from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # 소켓을 통해 들어온 데이터 각 소켓으로 전송하는 역할.  
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        

manager = ConnectionManager()