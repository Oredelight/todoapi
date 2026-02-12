from fastapi import FastAPI
from handlers import routes
from database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)