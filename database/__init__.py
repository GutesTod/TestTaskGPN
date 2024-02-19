import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    "postgresql+psycopg:///example.db"
)

engine.connect()

Base = declarative_base()

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

