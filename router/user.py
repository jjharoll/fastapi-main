from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/', response_model = UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get('/')
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)

@router.get('/{id}',response_model = UserDisplay)
def get_user(id,db: Session = Depends(get_db)):
    return db_user.get_user(db,id)

@router.put('/{id}/update')
def update_user(id:int, request: UserBase,db: Session = Depends(get_db)):
    return db_user.update_user(db,id,request)

@router.delete('/delete/{id}')
def delete(id:int,db: Session = Depends(get_db)):
    return db_user.delete_user(db,id)



    