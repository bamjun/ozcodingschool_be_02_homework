from pydantic import BaseModel
from typing import List

# pydantic -> 데이터 유효성 검증

class Item(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str

    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능.  

class UserBase(BaseModel):
    email: str



class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능.


class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None