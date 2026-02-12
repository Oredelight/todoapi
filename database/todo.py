from sqlalchemy.orm import Session
from database.model import Todos
from database.schemas import TodoCreate

def create_todo(db:Session, todo:TodoCreate):
    todos = Todos(description=todo.description, status=todo.status, owner_id=todo.owner_id)
    db.add(todos)
    db.commit()
    return todos

def update_todo(db:Session, id:int, todo:TodoCreate):
    existing_todo = db.query(Todos).filter_by(id=id).first()
    if not existing_todo:
        return None

    existing_todo.description = todo.description
    existing_todo.status = todo.status

    db.commit()
    return existing_todo

def delete_todo(db:Session, id:int):
    todo = db.query(Todos).filter_by(id=id).first()
    if not todo:
        return None
    
    db.delete(todo)
    db.commit()
    return todo

def get_todos(db:Session):
    todos = db.query(Todos).all()
    return todos

def get_todo(db:Session, id: int):
    todo = db.query(Todos).filter_by(id=id).first()
    return todo

def get_user_todo(db:Session, owner_id: int):
    user_todo = db.query(Todos).filter_by(owner_id=owner_id).all()
    return user_todo