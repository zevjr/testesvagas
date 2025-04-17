import pytest
from app.modules.calculator.domain.value_objects import Car, Coverage


class TestCar:
    """
    Test suite for the Car value object.
    Tests initialization and property access.
    """

    def test_car_initialization(self):
        """
        Test the Car initialization.
        
        This test verifies that the Car class correctly initializes with the provided values
        and that the properties can be accessed.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2020
        value = 50000.0
        
        # Act
        car = Car(make=make, model=model, year=year, value=value)
        
        # Assert
        assert car.make == make
        assert car.model == model
        assert car.year == year
        assert car.value == value

    def test_car_with_minimum_values(self):
        """
        Test the Car initialization with minimum values.
        
        This test verifies that the Car class correctly initializes with minimum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 1900  # Minimum reasonable year
        value = 0.0  # Minimum value
        
        # Act
        car = Car(make=make, model=model, year=year, value=value)
        
        # Assert
        assert car.make == make
        assert car.model == model
        assert car.year == year
        assert car.value == value

    def test_car_with_maximum_values(self):
        """
        Test the Car initialization with maximum values.
        
        This test verifies that the Car class correctly initializes with maximum values,
        which is an important edge case to test.
        """
        # Arrange
        make = "Toyota"
        model = "Corolla"
        year = 2100  # Maximum reasonable year
        value = 1000000.0  # Maximum reasonable value
        
        # Act
        car = Car(make=make, model=model, year=year, value=value)
        
        # Assert
        assert car.make == make
        assert car.model == model
        assert car.year == year
        assert car.value == value


class TestCoverage:
    """
    Test suite for the Coverage value object.
    Tests initialization and property access.
    """

    def test_coverage_initialization(self):
        """
        Test the Coverage initialization.
        
        This test verifies that the Coverage class correctly initializes with the provided values
        and that the properties can be accessed.
        """
        # Arrange
        deductible_percentage = 0.1
        broker_fee = 100.0
        registration_location = "New York"
        
        # Act
        coverage = Coverage(
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location
        )
        
        # Assert
        assert coverage.deductible_percentage == deductible_percentage
        assert coverage.broker_fee == broker_fee
        assert coverage.registration_location == registration_location

    def test_coverage_without_location(self):
        """
        Test the Coverage initialization without a registration location.
        
        This test verifies that the Coverage class correctly initializes without a registration location,
        which is an optional field.
        """
        # Arrange
        deductible_percentage = 0.1
        broker_fee = 100.0
        
        # Act
        coverage = Coverage(
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee
        )
        
        # Assert
        assert coverage.deductible_percentage == deductible_percentage
        assert coverage.broker_fee == broker_fee
        assert coverage.registration_location is None

    def test_coverage_with_minimum_values(self):
        """
        Test the Coverage initialization with minimum values.
        
        This test verifies that the Coverage class correctly initializes with minimum values,
        which is an important edge case to test.
        """
        # Arrange
        deductible_percentage = 0.0  # Minimum deductible
        broker_fee = 0.0  # Minimum broker fee
        
        # Act
        coverage = Coverage(
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee
        )
        
        # Assert
        assert coverage.deductible_percentage == deductible_percentage
        assert coverage.broker_fee == broker_fee
        assert coverage.registration_location is None

    def test_coverage_with_maximum_values(self):
        """
        Test the Coverage initialization with maximum values.
        
        This test verifies that the Coverage class correctly initializes with maximum values,
        which is an important edge case to test.
        """
        # Arrange
        deductible_percentage = 1.0  # Maximum deductible
        broker_fee = 1000.0  # Maximum reasonable broker fee
        registration_location = "New York"
        
        # Act
        coverage = Coverage(
            deductible_percentage=deductible_percentage,
            broker_fee=broker_fee,
            registration_location=registration_location
        )
        
        # Assert
        assert coverage.deductible_percentage == deductible_percentage
        assert coverage.broker_fee == broker_fee
        assert coverage.registration_location == registration_location 