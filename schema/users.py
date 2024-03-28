from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class UserUpdate(User):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponse(User):
    pass
