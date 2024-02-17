from fastapi import APIRouter
from web.models import Value

router = APIRouter()

@router.get("/data/get")
def get_data():
    ...
    
@router.post("/data/upload")
def upload_data():
    ...

