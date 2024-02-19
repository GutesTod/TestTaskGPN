from fastapi import FastAPI
from web import test_router
from database import Base, engine
from sqlalchemy_utils import database_exists, create_database

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(test_router)
