from pydantic import BaseModel
from typing import List

# pydantic -> 데이터 유효성 검증

class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능.  

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None

    # from typing import Optional
    # title: Optional[str] = None
    # description: Optional[str] = None



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
    # 3.10 버전 이하는 아래처럼
    # from typing import Optional
    # email: Optional[str] | None = None
    # password: Optional[str] | None = None