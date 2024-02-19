from fastapi import FastAPI
from web import test_router
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(test_router)
