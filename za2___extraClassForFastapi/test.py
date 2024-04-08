import asyncio


async def wait(wait_time: int, identifier: str | int) -> str | int:
    print(f"[{identifier}] {wait_time} 만큼 기다리기 시작!")
    await asyncio.sleep(wait_time)
    print(f"[{identifier}] {wait_time} 만큼 기다리기 종료!")
    return identifier


async def main():
    result1, result2, result3 = await asyncio.gather(
        wait(3, "첫번째"),
        wait(2, "두번째"),
        wait(1, "세번째"),
    )
    print(result1, result2, result3)

asyncio.run(main())
