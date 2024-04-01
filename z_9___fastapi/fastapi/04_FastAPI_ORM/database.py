from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 동기용 데이터 베이스 접속 명령어 (pymysql)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1Rlaqjawns%4018@localhost/oz-fastapi'
engin = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engin)


# 비동기용 데이터 베이스 접속 명령어(aiomysql)
# 무거운 I/O dycjddl ajswj dhkeh, enldp rkqudns i/o 작업요청이 들어오면 가벼운 요청이 먼저 응답한다.
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
ASYNC_SQLALCHEMY_DATABASE_URI = 'mysql+aiomysql://root:1Rlaqjawns%4018@localhost/oz-fastapi'
engin = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URI)
AsyncSessionLocal =  sessionmaker(bind=engin, class_=AsyncSession)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

