import pytest
from app.modules.calculator.presentation import PremiumRequest, PremiumResponse


class TestPremiumRequest:
    """
    Test suite for the PremiumRequest model.
    Tests initialization and property access.
    """

    def test_request_initialization(self):
        """
        Test the PremiumRequest initialization.
        
        This test verifies that the PremiumRequest class correctly initializes with the provided values
        and that the properties can be accessed.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2020
        value = 50000.0
        deductible_percentage = 0.1
        broker_fee = 100.0
        registration_location = "New York"
        
        # Act
        request = PremiumRequest(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location
        )
        
        # Assert
        assert request.make == make
        assert request.model == model
        assert request.year == year
        assert request.value == value
        assert request.deductible_percentage == deductible_percentage
        assert request.broker_fee == broker_fee
        assert request.registration_location == registration_location

    def test_request_without_location(self):
        """
        Test the PremiumRequest initialization without a registration location.
        
        This test verifies that the PremiumRequest class correctly initializes without a registration location,
        which is an optional field.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2020
        value = 50000.0
        deductible_percentage = 0.1
        broker_fee = 100.0
        
        # Act
        request = PremiumRequest(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=None
        )
        
        # Assert
        assert request.make == make
        assert request.model == model
        assert request.year == year
        assert request.value == value
        assert request.deductible_percentage == deductible_percentage
        assert request.broker_fee == broker_fee
        assert request.registration_location is None

    def test_request_with_minimum_values(self):
        """
        Test the PremiumRequest initialization with minimum values.
        
        This test verifies that the PremiumRequest class correctly initializes with minimum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 1900  # Minimum reasonable year
        value = 0.0  # Minimum value
        deductible_percentage = 0.0  # Minimum deductible
        broker_fee = 0.0  # Minimum broker fee
        
        # Act
        request = PremiumRequest(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=None
        )
        
        # Assert
        assert request.make == make
        assert request.model == model
        assert request.year == year
        assert request.value == value
        assert request.deductible_percentage == deductible_percentage
        assert request.broker_fee == broker_fee
        assert request.registration_location is None

    def test_request_with_maximum_values(self):
        """
        Test the PremiumRequest initialization with maximum values.
        
        This test verifies that the PremiumRequest class correctly initializes with maximum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2100  # Maximum reasonable year
        value = 1000000.0  # Maximum reasonable value
        deductible_percentage = 1.0  # Maximum deductible
        broker_fee = 1000.0  # Maximum reasonable broker fee
        registration_location = "New York"
        
        # Act
        request = PremiumRequest(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location
        )
        
        # Assert
        assert request.make == make
        assert request.model == model
        assert request.year == year
        assert request.value == value
        assert request.deductible_percentage == deductible_percentage
        assert request.broker_fee == broker_fee
        assert request.registration_location == registration_location


class TestPremiumResponse:
    """
    Test suite for the PremiumResponse model.
    Tests initialization and property access.
    """

    def test_response_initialization(self):
        """
        Test the PremiumResponse initialization.
        
        This test verifies that the PremiumResponse class correctly initializes with the provided values
        and that the properties can be accessed.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2020
        value = 50000.0
        deductible_percentage = 0.1
        broker_fee = 100.0
        registration_location = "New York"
        applied_rate = 0.05
        calculated_premium = 2600.0
        policy_limit = 45000.0
        deductible_value = 5000.0
        
        # Act
        response = PremiumResponse(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location,
            applied_rate=applied_rate,
            calculated_premium=calculated_premium,
            policy_limit=policy_limit,
            deductible_value=deductible_value
        )
        
        # Assert
        assert response.make == make
        assert response.model == model
        assert response.year == year
        assert response.value == value
        assert response.deductible_percentage == deductible_percentage
        assert response.broker_fee == broker_fee
        assert response.registration_location == registration_location
        assert response.applied_rate == applied_rate
        assert response.calculated_premium == calculated_premium
        assert response.policy_limit == policy_limit
        assert response.deductible_value == deductible_value

    def test_response_without_location(self):
        """
        Test the PremiumResponse initialization without a registration location.
        
        This test verifies that the PremiumResponse class correctly initializes without a registration location,
        which is an optional field.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2020
        value = 50000.0
        deductible_percentage = 0.1
        broker_fee = 100.0
        applied_rate = 0.05
        calculated_premium = 2600.0
        policy_limit = 45000.0
        deductible_value = 5000.0
        
        # Act
        response = PremiumResponse(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=None,
            applied_rate=applied_rate,
            calculated_premium=calculated_premium,
            policy_limit=policy_limit,
            deductible_value=deductible_value
        )
        
        # Assert
        assert response.make == make
        assert response.model == model
        assert response.year == year
        assert response.value == value
        assert response.deductible_percentage == deductible_percentage
        assert response.broker_fee == broker_fee
        assert response.registration_location is None
        assert response.applied_rate == applied_rate
        assert response.calculated_premium == calculated_premium
        assert response.policy_limit == policy_limit
        assert response.deductible_value == deductible_value

    def test_response_with_minimum_values(self):
        """
        Test the PremiumResponse initialization with minimum values.
        
        This test verifies that the PremiumResponse class correctly initializes with minimum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 1900  # Minimum reasonable year
        value = 0.0  # Minimum value
        deductible_percentage = 0.0  # Minimum deductible
        broker_fee = 0.0  # Minimum broker fee
        applied_rate = 0.0  # Minimum applied rate
        calculated_premium = 0.0  # Minimum calculated premium
        policy_limit = 0.0  # Minimum policy limit
        deductible_value = 0.0  # Minimum deductible value
        
        # Act
        response = PremiumResponse(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=None,
            applied_rate=applied_rate,
            calculated_premium=calculated_premium,
            policy_limit=policy_limit,
            deductible_value=deductible_value
        )
        
        # Assert
        assert response.make == make
        assert response.model == model
        assert response.year == year
        assert response.value == value
        assert response.deductible_percentage == deductible_percentage
        assert response.broker_fee == broker_fee
        assert response.registration_location is None
        assert response.applied_rate == applied_rate
        assert response.calculated_premium == calculated_premium
        assert response.policy_limit == policy_limit
        assert response.deductible_value == deductible_value

    def test_response_with_maximum_values(self):
        """
        Test the PremiumResponse initialization with maximum values.
        
        This test verifies that the PremiumResponse class correctly initializes with maximum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2100  # Maximum reasonable year
        value = 1000000.0  # Maximum reasonable value
        deductible_percentage = 1.0  # Maximum deductible
        broker_fee = 1000.0  # Maximum reasonable broker fee
        registration_location = "New York"
        applied_rate = 1.0  # Maximum reasonable applied rate
        calculated_premium = 1000000.0  # Maximum reasonable calculated premium
        policy_limit = 1000000.0  # Maximum reasonable policy limit
        deductible_value = 1000000.0  # Maximum reasonable deductible value
        
        # Act
        response = PremiumResponse(
            make=make,
            model=model,
            year=year,
            value=value,
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location,
            applied_rate=applied_rate,
            calculated_premium=calculated_premium,
            policy_limit=policy_limit,
            deductible_value=deductible_value
        )
        
        # Assert
        assert response.make == make
        assert response.model == model
        assert response.year == year
        assert response.value == value
        assert response.deductible_percentage == deductible_percentage
        assert response.broker_fee == broker_fee
        assert response.registration_location == registration_location
        assert response.applied_rate == applied_rate
        assert response.calculated_premium == calculated_premium
        assert response.policy_limit == policy_limit
        assert response.deductible_value == deductible_value 