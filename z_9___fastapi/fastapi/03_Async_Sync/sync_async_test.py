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


# 피보나치 수열 -> 무거울 연산 작업
# CPU에 부화가 걸리는 작업 (복잡한 연산): 동기
# I/O: 비동기
def cpu_intensive_task():
    def fibonecci(n):
        if n <= 1:
            return n
        else:
            return fibonecci(n - 1) + fibonecci(n - 2)
        
    result = fibonecci(25)
    return result

# Worst Case 성능 저하 발생 : cpu 부하 > Event Loop부하가 걸림.  
# 1 1 2 3 5 8 13 21 34 55 89
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {'msg': result}

# good case
# CPU에 부하가 많이 걸리는 작업은 이벤트 루프에서 분리후, 별도의 프로세서에서 실행하게 만들어준다.
from concurrent.futures import ThreadPoolExecutor
def cpu_bound_task():
    with ThreadPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(
                executor, 
                cpu_intensive_task
            )
    return {'result': result}
