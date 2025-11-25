from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    user = models.User(
        email=user_in.email,
        full_name=user_in.full_name,
        is_active=user_in.is_active,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, user_in: schemas.UserUpdate):
    user = get_user(db, user_id)
    if not user:
        return None

    update_data = user_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> bool:
    user = get_user(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
