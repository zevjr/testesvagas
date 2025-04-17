from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass


@dataclass(frozen=True)
class PremiumRequest(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None