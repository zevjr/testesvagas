from app.main import create_app
import pytest
from unittest.mock import MagicMock, patch
import os
import sys
from fastapi.testclient import TestClient

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock environment variables for testing
@pytest.fixture(autouse=True)
def mock_env_vars():
    """
    Automatically mock environment variables for all tests.
    This ensures consistent test behavior regardless of the actual environment.
    """
    with patch.dict(os.environ, {
        'COVERAGE_PERCENTAGE': '1.0',
        'AGE_RATE_INCREMENT': '0.005',
        'VALUE_RATE_INCREMENT': '0.005',
        'VALUE_INCREMENT_STEP': '10000',
        'MIN_GIS_ADJUSTMENT': '-0.02',
        'MAX_GIS_ADJUSTMENT': '0.02'
    }):
        yield

# Mock datetime for consistent testing
@pytest.fixture(autouse=True)
def mock_datetime():
    """
    Automatically mock datetime for all tests.
    This ensures consistent test behavior regardless of the actual date.
    """
    with patch('datetime.datetime') as mock_datetime:
        # Set a fixed date for all tests
        mock_datetime.now.return_value.year = 2023
        yield mock_datetime

@pytest.fixture
def client():
    """Fixture providing a TestClient instance"""
    app = create_app()
    return TestClient(app)

@pytest.fixture
def valid_request_data():
    """Fixture providing valid request data"""
    return {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "value": 50000.0,
        "deductible_percentage": 0.1,
        "broker_fee": 100.0,
        "registration_location": "New York"
    }

@pytest.fixture
def valid_response_data():
    """Fixture providing valid response data"""
    return {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "value": 50000.0,
        "deductible_percentage": 0.1,
        "broker_fee": 100.0,
        "registration_location": "New York",
        "applied_rate": 0.05,
        "calculated_premium": 2600.0,
        "policy_limit": 45000.0,
        "deductible_value": 5000.0
    }
