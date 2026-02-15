from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database.schemas import UserCreate, UserOut, TodoOut, TodoCreate, LoginRequest
from fastapi.security import OAuth2PasswordRequestForm
from handlers.auth import create_access_token
from database.db import get_db
from typing import List
from database.user import get_user_by_email, create_user, get_user, delete_user, get_all, authenticate_user
from database.todo import create_todo, update_todo, delete_todo, get_todos, get_todo, get_user_todo

router = APIRouter()

@router.post("/register_user", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def Create_new_user(user:UserCreate, db:Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return create_user(db=db, user=user)

@router.post("/login")
def login_for_access_token(login_data:LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(email = login_data.email, password=login_data.password, db=db)
    if not user:
        raise HTTPException(status_code=404, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/{user_id}", response_model=UserOut)
def get_user_by_id(user_id:int, db:Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=List[UserOut], status_code=200)
def get_all_users(db:Session = Depends(get_db)):
    return get_all(db=db)

@router.delete("/users/{user_id}", status_code=200)
def delete_user_by_id(user_id: int, db:Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    return {"message": "User deleted succcessfully"}

@router.post("/create_todo", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def Create_new_todo(todo:TodoCreate, db:Session = Depends(get_db)):
    todo = create_todo(db=db, todo=todo)
    return todo

@router.put("/update_todo/{todo_id}", response_model=TodoOut)
def update_todo_by_id(todo:TodoCreate, id:int, db:Session = Depends(get_db)):
    updated_todo = update_todo(db=db, id=id, todo=todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return updated_todo

@router.get("/todos", response_model=List[TodoOut], status_code=200)
def get_all_todos(db:Session = Depends(get_db)):
    return get_todos(db=db)

@router.delete("/todos/{todo_id}", status_code=200)
def delete_todo_by_id(todo_id:int, db:Session = Depends(get_db)):
    todo = delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo does not exist")
    
    return {"message": "Todo deleted successfully"}

@router.get("/todo/{todo_id}", response_model=TodoOut)
def get_todo_by_id(todo_id:int, db:Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/users/{owner_id}/todos", response_model=List[TodoOut])
def get_todo_by_userid(owner_id:int, db:Session = Depends(get_db)):
    todos = get_user_todo(db, owner_id)
    if not todos:
        return []
    
    return todos
