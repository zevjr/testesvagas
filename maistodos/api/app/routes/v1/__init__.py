from fastapi import APIRouter
from app.views import router_health



api_router_v1 = APIRouter()

api_router_v1.include_router(
    router_health,
    prefix="/health",
    tags=["health"],
)

