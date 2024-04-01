from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_db
from schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session
import crud_orm

router = APIRouter()

@router.post('/')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_orm.create_user(db=db, user=user)
    return db_user

from typing import Union
#api/v1/user/{user_id} or {user_data}
@router.get('/{user_data}')
def get_user(user_data: Union[int, str], db: Session = Depends(get_db)):
    try:
        user_data = int(user_data)
        db_user = crud_orm.get_user_id(db, user_data)
    except:
        db_user = crud_orm.get_user_email(db, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get('/')
def get_users(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud_orm.get_users(db, skip, limit)

@router.put('/{users_id}')
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud_orm.update_user(db, user_id, user_update)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


def delete_user(): pass