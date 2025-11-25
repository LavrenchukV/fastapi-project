from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from .database import Base, engine, get_db
from . import schemas, crud, models

# Base.metadata.create_all(bind=engine) 
# for now I use Alembic, that's why I commented this part of code

app = FastAPI(title="Week 1 CRUD API")


@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/users/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user_in)


@app.get("/users/", response_model=List[schemas.UserRead])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@app.put("/users/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, user_in: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id=user_id, user_in=user_in)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_user(db, user_id)
    if not ok:
        raise HTTPException(404, "User not found")
    return
