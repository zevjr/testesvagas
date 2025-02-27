import pytest
from app import create_app
from app.database import db

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()
