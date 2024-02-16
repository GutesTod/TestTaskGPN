from fastapi import APIRouter

router = APIRouter()

@router.get("/data/get")
def get_data():
    ...
    
@router.post("/data/upload")
def upload_data():
    ...
