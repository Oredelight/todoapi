from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class TodoCreate(BaseModel):
    description: str
    status: str
    owner_id: int

class TodoOut(BaseModel):
    id: int
    description: str
    status: str
    owner_id: int


