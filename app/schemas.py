from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = None          # the second migration - add age-column


class UserCreate(UserBase):
    password: str                      # plain password comes only here


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    age: Optional[int] = None          # the second migration - add age-column


class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
