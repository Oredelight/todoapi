from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database.model import User
from database.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username:str, password: str, db):
    user = db.query(User).filter_by(username=username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db:Session, id: int):
    user = db.query(User).filter_by(id=id).first()
    return user

def get_all(db:Session):
    users = db.query(User).all()
    return users

def delete_user(db:Session, id: int):
    user = db.query(User).filter_by(id=id).first()
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user

def get_user_by_email(db: Session, email:str):
    return db.query(User).filter_by(email=email).first()
