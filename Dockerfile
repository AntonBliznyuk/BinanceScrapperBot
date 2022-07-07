FROM python:3.9.6

WORKDIR /
COPY crypto_bot crypto_bot
COPY app.py app.py

# install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# set DB credentials
ARG ARG_PG_DB_NAME=postgres
ARG ARG_PG_DB_PASSWORD=postgres
ARG ARG_PG_DB_USER=postgres
ARG ARG_PG_DB_HOST=pg_db

ENV PG_DB_NAME=$ARG_PG_DB_NAME
ENV PG_DB_PASSWORD=$ARG_PG_DB_PASSWORD
ENV PG_DB_USER=$ARG_PG_DB_USER
ENV PG_DB_HOST=$ARG_PG_DB_HOST

CMD ["python", "app.py"]