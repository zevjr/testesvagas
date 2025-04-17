# Car Insurance Premium Simulator

## About the Project

This project is a Car Insurance Premium Simulator that calculates insurance premiums based on various factors such as age, vehicle value, and other risk factors. It's designed as a technical assessment for GX2, demonstrating modern software development practices and architectural decisions.

The simulator provides a REST API that allows users to calculate insurance premiums by considering multiple factors and applying specific business rules for premium adjustments.

## Technical Assessment Context

This project was developed as part of a technical assessment for GX2, showcasing:
- Clean Architecture and Domain-Driven Design (DDD) principles
- Modern Python development practices
- API development with FastAPI
- Test-driven development
- Docker containerization
- Poetry for dependency management

## Technical Decisions

### Domain-Driven Design (DDD)
The project follows DDD principles for several reasons:
1. **Clear Business Domain**: Insurance premium calculation is a complex domain with specific business rules and entities
2. **Maintainability**: DDD helps organize code around business concepts, making it easier to maintain and evolve
3. **Testability**: The domain layer can be tested independently of infrastructure concerns
4. **Separation of Concerns**: Clear boundaries between domain logic, application services, and infrastructure

### Architecture
The project structure follows a clean architecture approach:
- **Domain Layer**: Core business logic and entities
- **Application Layer**: Use cases and business rules
- **Infrastructure Layer**: External services and implementations
- **Presentation Layer**: API endpoints and controllers

### Technology Stack
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Poetry**: Dependency management and packaging
- **Docker**: Containerization for consistent environments
- **Pytest**: Testing framework with async support

## Getting Started

### Prerequisites

#### Using Poetry (Recommended)
1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

#### Using Docker
1. Install Docker and Docker Compose:
```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io docker-compose
```

2. Build and run the container:
```bash
docker-compose up --build
```

### Running the Application

#### With Poetry
```bash
poetry run uvicorn app.main:app --reload
```

#### With Docker
The application will be available at `http://localhost:8000` after running `docker-compose up`

### Running Tests

#### With Poetry
```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=app tests/

# Generate coverage report
poetry run coverage html
```

#### With Docker
```bash
docker-compose run app pytest
```

## API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

The following environment variables can be configured:
- `COVERAGE_PERCENTAGE`: Base coverage percentage
- `AGE_RATE_INCREMENT`: Rate increment for age factor
- `VALUE_RATE_INCREMENT`: Rate increment for vehicle value
- `VALUE_INCREMENT_STEP`: Step value for vehicle value increments
- `MIN_GIS_ADJUSTMENT`: Minimum GIS adjustment
- `MAX_GIS_ADJUSTMENT`: Maximum GIS adjustment

## Project Structure

```
app/
├── common/          # Shared utilities and helpers
├── config/          # Configuration management
├── modules/         # Application modules
│   ├── insurance/   # Insurance domain module
│   └── ...         # Other modules
└── main.py         # Application entry point
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
