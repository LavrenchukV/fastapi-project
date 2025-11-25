from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    age: Optional[int] = None          # the second migration - add age-colunm

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    age: Optional[int] = None          # the second migration - add age-colunm

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
