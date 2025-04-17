from datetime import datetime

from app.config.config import settings
from app.config.logger import Logger
from app.modules.calculator.domain.value_objects import Car, Coverage
from app.modules.calculator.presentation import PremiumRequest, PremiumResponse


class BasePremiumService:
    @property
    def _car_age(self) -> int:
        return datetime.now().year - self._car.year

    @property
    def _age_rate_increment(self) -> float:
        return settings.AGE_RATE_INCREMENT

    @property
    def _value_rate_increment(self) -> float:
        return settings.VALUE_RATE_INCREMENT

    @property
    def _value_increment_step(self) -> float:
        return settings.VALUE_INCREMENT_STEP

    @property
    def _coverage_percentage(self) -> float:
        return settings.COVERAGE_PERCENTAGE

    @property
    def _min_gis(self) -> float:
        return settings.MIN_GIS_ADJUSTMENT

    @property
    def _max_gis(self) -> float:
        return settings.MAX_GIS_ADJUSTMENT



class PremiumService(BasePremiumService):
    def __init__(self, request: PremiumRequest) -> None:
        self._request = request
        self._car = self._build_car()
        self._coverage = self._build_coverage()
        self.logger = Logger(PremiumService.__name__)

    def calculate(self) -> PremiumResponse:
        self.logger.info("Start calculate method")
        applied_rate = self._calculate_applied_rate()
        base_premium = self._car.value * applied_rate
        deductible_discount = base_premium * self._coverage.deductible_percentage
        calculated_premium = base_premium - deductible_discount + self._coverage.broker_fee

        base_policy_limit = self._car.value * self._coverage_percentage
        deductible_value = base_policy_limit * self._coverage.deductible_percentage
        final_policy_limit = base_policy_limit - deductible_value

        
        self.logger.info("End calculate method")
        return PremiumResponse(
            make=self._car.make,
            model=self._car.model,
            year=self._car.year,
            value=self._car.value,
            deductible_percentage=self._coverage.deductible_percentage,
            broker_fee=self._coverage.broker_fee,
            registration_location=self._coverage.registration_location,
            applied_rate=applied_rate,
            calculated_premium=calculated_premium,
            policy_limit=final_policy_limit,
            deductible_value=deductible_value,
        )

    def _calculate_applied_rate(self) -> float:
        age_component = self._car_age * self._age_rate_increment
        value_component = (self._car.value // self._value_increment_step) * self._value_rate_increment
        gis_adjustment = self._calculate_gis_adjustment()
        return age_component + value_component + gis_adjustment

    def _calculate_gis_adjustment(self) -> float:
        if not self._coverage.registration_location:
            return 0.0

        risk_factor = (hash(self._coverage.registration_location) % 5) / 100 - 0.02
        return max(min(risk_factor, self._max_gis), self._min_gis)

    def _build_car(self) -> Car:
        return Car(
            make=self._request.make,
            model=self._request.model,
            year=self._request.year,
            value=self._request.value,
        )

    def _build_coverage(self) -> Coverage:
        return Coverage(
            deductible_percentage=self._request.deductible_percentage,
            broker_fee=self._request.broker_fee,
            registration_location=self._request.registration_location,
        )

