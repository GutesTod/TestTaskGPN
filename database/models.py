from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# Модель данных для пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)

# Модель данных для устройства
class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    
    users = relationship(User)

# Модель данных для измерения
class Value(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    timestamp = Column(String)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    
    device = relationship(Device)