from pydantic import BaseModel, Field
from typing import Optional

class PremiumResponse(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None
    applied_rate: float = Field(round=3)
    policy_limit: float
    deductible_value: float
    calculated_premium: float = Field(round=2)