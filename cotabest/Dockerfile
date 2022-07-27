FROM python:3.10.5-slim

ENV PYTHONUNBUFFERED=1 
ENV POETRY_VIRTUALENVS_IN_PROJECT=true 
ENV POETRY_HOME="/opt/poetry" 
ENV POETRY_NO_INTERACTION=1 
ENV PYSETUP_PATH="/opt/pysetup" 
ENV VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False
ENV SWAGGER_URL="http://localhost:5000"
ENV SQLALCHEMY_DATABASE_URI="sqlite:///develop.db"


RUN apt-get update\
    && apt-get install --no-install-recommends -y\
    curl\
    build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app
COPY . .

RUN poetry install --no-dev

EXPOSE 5000

RUN poetry run flask utils populate

CMD ["poetry","run","gunicorn","src.app:create_app()","--bind","0.0.0.0:5000"]

