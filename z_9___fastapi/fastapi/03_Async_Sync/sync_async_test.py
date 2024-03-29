from fastapi import APIRouter
import time

router = APIRouter()


@router.get('/slow-sync-ping')
def slow_sync_ping():
    # 초마다 작업..  
    time.sleep(10)

    return {'msg': 'pong'}


import asyncio
@router.get('/slow-async-ping')
async def slow_async_ping():
    # 비동기로 작업 비동기로 작업.  
    # 다른작업들은 계속 된다.
    await asyncio.sleep(10)

    return {'msg': 'pong'}
