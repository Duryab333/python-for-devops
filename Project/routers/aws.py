from fastapi import APIRouter, HTTPException
from services.aws_service import get_bucket_info

router = APIRouter()

@router.get("/s3", status_code=200)
def get_bucket():
    try:
        bucket_info = get_bucket_info()
        return bucket_info
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail="Internal Server Error"
        )





@router.get("/ec2", status_code=200)
def get_instances():
    try:
        return  {"message": "ec2 utilities in progess ..."}
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail="Internal Server Error"
        )




