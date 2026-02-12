from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    hashed_password=Column(String, nullable=True)
    created_at=Column(DateTime, server_default=func.now())

    todos = relationship("Todos", back_populates="owner", cascade="all, delete")

class Todos(Base):
    __tablename__= "todos"

    id=Column(Integer, primary_key=True)
    description=Column(Text)
    status=Column(String, nullable=False)
    owner_id=Column(Integer, ForeignKey("users.id"))
    created_at=Column(DateTime, server_default=func.now())
    updated_at=Column(DateTime, server_default=func.now())

    owner = relationship("User", back_populates=("todos"))

