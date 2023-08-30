import logging

from fastapi import APIRouter

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/")
async def list_all_credit_card():
    return {"message": "OK"}


@router.get("/{key}")
async def get_credit_card_for_key(key: str):
    return {"message": "key: " + key}


@router.post("/")
async def create_credit():
    return {"message": "created"}
