from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserPublic(UserBase):
    username: str


class UserLogin(UserBase):
    password: str


class UserCreate(UserBase):
    username: str
    password: str


class UserDB(UserCreate):
    id: str