from pydantic import BaseModel

class Value(BaseModel):
    deviceId: int
    x: float
    y: float
    z: float
    time: float