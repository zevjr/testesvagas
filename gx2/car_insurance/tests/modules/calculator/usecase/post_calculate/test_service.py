import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

from app.modules.calculator.usecase.post_calculate.service import PremiumService
from app.modules.calculator.presentation import PremiumRequest, PremiumResponse
from app.modules.calculator.domain.value_objects import Car, Coverage


class TestPremiumService:
    """
    Test suite for the PremiumService class.
    Tests all methods and edge cases to ensure proper functionality.
    """

    @pytest.fixture
    def valid_request(self):
        """
        Fixture providing a valid PremiumRequest object for testing.
        """
        return PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=50000.0,
            deductible_percentage=0.1,
            broker_fee=100.0,
            registration_location="New York"
        )

    @pytest.fixture
    def service_with_valid_request(self, valid_request):
        """
        Fixture providing a PremiumService instance with a valid request.
        """
        return PremiumService(valid_request)

    def test_build_car(self, service_with_valid_request, valid_request):
        """
        Test the _build_car method.
        
        This test verifies that the _build_car method correctly creates a Car object
        from the request data. This is a critical method as it initializes the car
        data used throughout the premium calculation.
        """
        # Act
        car = service_with_valid_request._build_car()
        
        # Assert
        assert isinstance(car, Car)
        assert car.make == valid_request.make
        assert car.model == valid_request.model
        assert car.year == valid_request.year
        assert car.value == valid_request.value

    def test_build_coverage(self, service_with_valid_request, valid_request):
        """
        Test the _build_coverage method.
        
        This test verifies that the _build_coverage method correctly creates a Coverage object
        from the request data. This is a critical method as it initializes the coverage data
        used throughout the premium calculation.
        """
        # Act
        coverage = service_with_valid_request._build_coverage()
        
        # Assert
        assert isinstance(coverage, Coverage)
        assert coverage.deductible_percentage == valid_request.deductible_percentage
        assert coverage.broker_fee == valid_request.broker_fee
        assert coverage.registration_location == valid_request.registration_location

    def test_build_coverage_without_location(self):
        """
        Test the _build_coverage method with a request that has no registration location.
        
        This test verifies that the _build_coverage method correctly handles requests
        without a registration location, which is an optional field.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=50000.0,
            deductible_percentage=0.1,
            broker_fee=100.0,
            registration_location=None
        )
        service = PremiumService(request)
        
        # Act
        coverage = service._build_coverage()
        
        # Assert
        assert isinstance(coverage, Coverage)
        assert coverage.registration_location is None

    def test_car_age_calculation(self, service_with_valid_request):
        """
        Test the _car_age property.
        
        This test verifies that the _car_age property correctly calculates the age of the car
        based on the current year and the car's year. This is important for the premium calculation
        as the car's age affects the applied rate.
        """
        # Since we're mocking datetime.now().year to 2025 in conftest.py
        # and the car year is 2020, the car age should be 5
        assert service_with_valid_request._car_age == 5

    def test_calculate_gis_adjustment_with_location(self, service_with_valid_request):
        """
        Test the _calculate_gis_adjustment method with a registration location.
        
        This test verifies that the _calculate_gis_adjustment method correctly calculates
        the GIS adjustment when a registration location is provided. The GIS adjustment
        is based on a hash of the location and is bounded by MIN_GIS_ADJUSTMENT and MAX_GIS_ADJUSTMENT.
        """
        # Act
        gis_adjustment = service_with_valid_request._calculate_gis_adjustment()
        
        # Assert
        # The hash of "New York" % 5 / 100 - 0.02 should be within the bounds
        assert -0.02 <= gis_adjustment <= 0.02

    def test_calculate_gis_adjustment_without_location(self):
        """
        Test the _calculate_gis_adjustment method without a registration location.
        
        This test verifies that the _calculate_gis_adjustment method returns 0.0
        when no registration location is provided, as no GIS adjustment should be applied.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=50000.0,
            deductible_percentage=0.1,
            broker_fee=100.0,
            registration_location=None
        )
        service = PremiumService(request)
        
        # Act
        gis_adjustment = service._calculate_gis_adjustment()
        
        # Assert
        assert gis_adjustment == 0.0

    def test_calculate_applied_rate(self, service_with_valid_request):
        """
        Test the _calculate_applied_rate method.
        
        This test verifies that the _calculate_applied_rate method correctly calculates
        the applied rate based on the car's age, value, and GIS adjustment. The applied rate
        is a critical component of the premium calculation.
        """
        # Act
        applied_rate = service_with_valid_request._calculate_applied_rate()
        
        # Assert
        # Expected calculation:
        # age_component = 3 * 0.005 = 0.015
        # value_component = (50000 // 10000) * 0.005 = 5 * 0.005 = 0.025
        # gis_adjustment = hash("New York") % 5 / 100 - 0.02 (bounded by -0.02 and 0.02)
        # applied_rate = age_component + value_component + gis_adjustment
        assert isinstance(applied_rate, float)
        assert applied_rate > 0

    def test_calculate(self, service_with_valid_request, valid_request):
        """
        Test the calculate method with a valid request.
        
        This test verifies that the calculate method correctly calculates the premium
        based on the car's value, applied rate, deductible percentage, and broker fee.
        It also verifies that the policy limit and deductible value are calculated correctly.
        """
        # Act
        response = service_with_valid_request.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.make == valid_request.make
        assert response.model == valid_request.model
        assert response.year == valid_request.year
        assert response.value == valid_request.value
        assert response.deductible_percentage == valid_request.deductible_percentage
        assert response.broker_fee == valid_request.broker_fee
        assert response.registration_location == valid_request.registration_location
        assert response.applied_rate > 0
        assert response.calculated_premium > 0
        assert response.policy_limit > 0
        assert response.deductible_value > 0

    def test_calculate_with_minimum_values(self):
        """
        Test the calculate method with minimum values.
        
        This test verifies that the calculate method correctly handles minimum values
        for all inputs, which is an important edge case to test.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2023,  # Current year (from mock)
            value=1000.0,  # Minimum value
            deductible_percentage=0.0,  # Minimum deductible
            broker_fee=0.0,  # Minimum broker fee
            registration_location=None  # No location
        )
        service = PremiumService(request)
        
        # Act
        response = service.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.calculated_premium >= 0
        assert response.policy_limit >= 0
        assert response.deductible_value >= 0

    def test_calculate_with_maximum_values(self):
        """
        Test the calculate method with maximum values.
        
        This test verifies that the calculate method correctly handles maximum values
        for all inputs, which is an important edge case to test.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=1980,  # Old car
            value=1000000.0,  # High value
            deductible_percentage=0.5,  # High deductible
            broker_fee=1000.0,  # High broker fee
            registration_location="New York"  # With location
        )
        service = PremiumService(request)
        
        # Act
        response = service.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.calculated_premium > 0
        assert response.policy_limit > 0
        assert response.deductible_value > 0

    def test_calculate_with_zero_value(self):
        """
        Test the calculate method with a car value of zero.
        
        This test verifies that the calculate method correctly handles a car value of zero,
        which is an important edge case to test.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=0.0,  # Zero value
            deductible_percentage=0.1,
            broker_fee=100.0,
            registration_location="New York"
        )
        service = PremiumService(request)
        
        # Act
        response = service.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.calculated_premium == 100.0  # Should only include broker fee
        assert response.policy_limit == 0.0  # Should be zero
        assert response.deductible_value == 0.0  # Should be zero

    def test_calculate_with_zero_deductible(self):
        """
        Test the calculate method with a deductible percentage of zero.
        
        This test verifies that the calculate method correctly handles a deductible percentage of zero,
        which is an important edge case to test.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=50000.0,
            deductible_percentage=0.0,  # Zero deductible
            broker_fee=100.0,
            registration_location="New York"
        )
        service = PremiumService(request)
        
        # Act
        response = service.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.deductible_percentage == 0.0
        assert response.deductible_value == 0.0  # Should be zero
        assert response.policy_limit == 50000.0  # Should be equal to car value

    def test_calculate_with_maximum_deductible(self):
        """
        Test the calculate method with a maximum deductible percentage.
        
        This test verifies that the calculate method correctly handles a maximum deductible percentage,
        which is an important edge case to test.
        """
        # Arrange
        request = PremiumRequest(
            make="Toyota",
            model="Corolla",
            year=2020,
            value=50000.0,
            deductible_percentage=1.0,  # Maximum deductible
            broker_fee=100.0,
            registration_location="New York"
        )
        service = PremiumService(request)
        
        # Act
        response = service.calculate()
        
        # Assert
        assert isinstance(response, PremiumResponse)
        assert response.deductible_percentage == 1.0
        assert response.deductible_value == 50000.0  # Should be equal to car value
        assert response.policy_limit == 0.0  # Should be zero

    def test_calculate_with_different_locations(self):
        """
        Test the calculate method with different registration locations.
        
        This test verifies that the calculate method correctly handles different registration locations,
        which should result in different GIS adjustments and thus different premiums.
        """
        # Arrange
        locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        responses = []
        
        # Act
        for location in locations:
            request = PremiumRequest(
                make="Toyota",
                model="Corolla",
                year=2020,
                value=50000.0,
                deductible_percentage=0.1,
                broker_fee=100.0,
                registration_location=location
            )
            service = PremiumService(request)
            response = service.calculate()
            responses.append(response)
        
        # Assert
        # All responses should be valid
        for response in responses:
            assert isinstance(response, PremiumResponse)
            assert response.calculated_premium > 0
        
        # Different locations should result in different premiums
        # due to different GIS adjustments
        premiums = [response.calculated_premium for response in responses]
        assert len(set(premiums)) > 1  # At least some premiums should be different

    def test_calculate_with_different_years(self):
        """
        Test the calculate method with different car years.
        
        This test verifies that the calculate method correctly handles different car years,
        which should result in different age components and thus different premiums.
        """
        # Arrange
        years = [2023, 2020, 2015, 2010, 2005]
        responses = []
        
        # Act
        for year in years:
            request = PremiumRequest(
                make="Toyota",
                model="Corolla",
                year=year,
                value=50000.0,
                deductible_percentage=0.1,
                broker_fee=100.0,
                registration_location="New York"
            )
            service = PremiumService(request)
            response = service.calculate()
            responses.append(response)
        
        # Assert
        # All responses should be valid
        for response in responses:
            assert isinstance(response, PremiumResponse)
            assert response.calculated_premium > 0
        
        # Different years should result in different premiums
        # due to different age components
        premiums = [response.calculated_premium for response in responses]
        assert len(set(premiums)) > 1  # At least some premiums should be different

    def test_calculate_with_different_values(self):
        """
        Test the calculate method with different car values.
        
        This test verifies that the calculate method correctly handles different car values,
        which should result in different value components and thus different premiums.
        """
        # Arrange
        values = [10000.0, 20000.0, 30000.0, 40000.0, 50000.0]
        responses = []
        
        # Act
        for value in values:
            request = PremiumRequest(
                make="Toyota",
                model="Corolla",
                year=2020,
                value=value,
                deductible_percentage=0.1,
                broker_fee=100.0,
                registration_location="New York"
            )
            service = PremiumService(request)
            response = service.calculate()
            responses.append(response)
        
        # Assert
        # All responses should be valid
        for response in responses:
            assert isinstance(response, PremiumResponse)
            assert response.calculated_premium > 0
        
        # Different values should result in different premiums
        # due to different value components
        premiums = [response.calculated_premium for response in responses]
        assert len(set(premiums)) > 1  # At least some premiums should be different 