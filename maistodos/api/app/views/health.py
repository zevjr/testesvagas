import logging

from fastapi import APIRouter


router = APIRouter()

logger = logging.getLogger(__name__)



@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/health")
async def health():
    return {"message": "OK"}