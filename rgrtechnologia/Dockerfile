FROM python:3

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

VOLUME local /app

RUN make install


ENTRYPOINT python -m pagescrap