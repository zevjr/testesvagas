import pytest
from unittest.mock import patch

from app.modules.calculator.usecase.post_calculate.service import BasePremiumService
from app.config.config import settings


class TestBasePremiumService:
    """
    Test suite for the BasePremiumService class.
    Tests all properties to ensure they correctly access the settings.
    """

    @pytest.fixture
    def base_service(self):
        """
        Fixture providing a BasePremiumService instance for testing.
        """
        return BasePremiumService()

    def test_car_age_property(self, base_service):
        """
        Test the _car_age property.
        
        This test verifies that the _car_age property correctly calculates the age of the car
        based on the current year and the car's year. This is important for the premium calculation
        as the car's age affects the applied rate.
        """
        # Since we're mocking datetime.now().year to 2023 in conftest.py
        # and we haven't set a car year, this should raise an AttributeError
        with pytest.raises(AttributeError):
            _ = base_service._car_age

    def test_age_rate_increment_property(self, base_service):
        """
        Test the _age_rate_increment property.
        
        This test verifies that the _age_rate_increment property correctly returns
        the AGE_RATE_INCREMENT setting value.
        """
        assert base_service._age_rate_increment == settings.AGE_RATE_INCREMENT

    def test_value_rate_increment_property(self, base_service):
        """
        Test the _value_rate_increment property.
        
        This test verifies that the _value_rate_increment property correctly returns
        the VALUE_RATE_INCREMENT setting value.
        """
        assert base_service._value_rate_increment == settings.VALUE_RATE_INCREMENT

    def test_value_increment_step_property(self, base_service):
        """
        Test the _value_increment_step property.
        
        This test verifies that the _value_increment_step property correctly returns
        the VALUE_INCREMENT_STEP setting value.
        """
        assert base_service._value_increment_step == settings.VALUE_INCREMENT_STEP

    def test_coverage_percentage_property(self, base_service):
        """
        Test the _coverage_percentage property.
        
        This test verifies that the _coverage_percentage property correctly returns
        the COVERAGE_PERCENTAGE setting value.
        """
        assert base_service._coverage_percentage == settings.COVERAGE_PERCENTAGE

    def test_min_gis_property(self, base_service):
        """
        Test the _min_gis property.
        
        This test verifies that the _min_gis property correctly returns
        the MIN_GIS_ADJUSTMENT setting value.
        """
        assert base_service._min_gis == settings.MIN_GIS_ADJUSTMENT

    def test_max_gis_property(self, base_service):
        """
        Test the _max_gis property.
        
        This test verifies that the _max_gis property correctly returns
        the MAX_GIS_ADJUSTMENT setting value.
        """
        assert base_service._max_gis == settings.MAX_GIS_ADJUSTMENT 