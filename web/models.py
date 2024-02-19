from pydantic import BaseModel, validator
from datetime import datetime


class ValueBase(BaseModel):
    x: float
    y: float
    z: float
    timestamp: datetime

    @validator("timestamp")
    def validate_timestamp(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            raise ValueError("Invalid timestamp format")
        return v
    
    class Config:
        orm_mode = True

class DeviceBase(BaseModel):
    name: str
    
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    
    class Config:
        orm_mode = True
    
class DeviceCreate(DeviceBase):
    user_id: int

class UserCreate(UserBase):
    pass

class ValueCreate(ValueBase):
    device_id: int
    
class ValueAnalysis(BaseModel):
    min_value: float
    max_value: float
    count: int
    sum_value: float
    median_value: float