from database import SessionLocal

# 동기용 의존성(세션 관리)
def get_db():
    db = SessionLocal()
    try:
        yield db  # 제너레이터
    finally:
        db.close()


# 비동기용 의존성(세션 관리)
from database import AsyncSessionLocal

def get_async_db():
    async def get_async_db():
        async with AsyncSessionLocal() as session:
            yield session