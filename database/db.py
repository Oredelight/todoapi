from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:password@localhost/Tasks"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
