from fastapi import APIRouter

from app.views import router_credit_card, router_health

api_router_v1 = APIRouter()

api_router_v1.include_router(
    router_health,
    prefix="/v1/health",
    tags=["health"],
)

api_router_v1.include_router(
    router_credit_card,
    prefix="/v1/credit-card",
    tags=["credit-card"],
)
