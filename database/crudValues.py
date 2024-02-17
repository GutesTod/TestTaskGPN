from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from database.models import Value
from datetime import datetime

def upload_data_x_y_z(db: Session, id: int, x: float, y: float, z: float, time: datetime):
    time = time.timestamp()
    result = db.execute(
        insert(Value),
        [
            {"deviceId": id, "x": x, "y": y, "z": z, "time": time}
        ]
    )
    
    return result.all()
    
def get_datas_x_y_z(db: Session, id: int, x: float, y: float, z: float):
    result = db.execute(
        select(Value).where(Value.device_id == id).order_by(Value.time)
    )
    return result.all()

