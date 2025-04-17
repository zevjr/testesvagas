from typing import Optional
from pydantic import BaseModel

class Car(BaseModel):
    make: str
    model: str
    year: int
    value: float

class Coverage(BaseModel):
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None