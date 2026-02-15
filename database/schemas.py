from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(min_length=8, max_length=72)

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

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


