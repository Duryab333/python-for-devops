from fastapi import APIRouter, HTTPException
from services.matrices_service import get_system_metics

router = APIRouter()

@router.get("/metrics", status_code=200)
def get_metrix():
    try:
        metrix = get_system_metics()
        return metrix
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail="Internal Server Error"
        )




