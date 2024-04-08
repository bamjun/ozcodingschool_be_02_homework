import asyncio
import time


async def hi(sleep_time: int, message: str):
    print(f"start {sleep_time} {message}")
    print(f'scheduled: {asyncio.get_event_loop()._scheduled}')
    print(f'ready: : {asyncio.get_event_loop()._ready}')
    await asyncio.sleep(sleep_time)
    print(f"end {sleep_time} {message}")
    print(f'scheduled: {asyncio.get_event_loop()._scheduled}')


async def main():
    print(f"started main at {time.strftime('%X')}")
    coros = [hi(i, str(i)) for i in range(1, 11)]
    await asyncio.gather(*coros)
    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())