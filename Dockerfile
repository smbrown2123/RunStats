# Build api image
FROM python:3.9 AS api

WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
COPY ./params.json   /code/params.json
COPY ./dbparams.json   /code/dbparams.json
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

# Copy the FastAPI app
COPY ./RunningAPI /code/RunningAPI

# Use Uvicorn to run the FastAPI app
CMD ["uvicorn", "RunningAPI.api:RunningAPI", "--host", "0.0.0.0", "--port", "80"]

# Build db image
FROM postgres:latest as db

COPY init/ /docker-entrypoint-initdb.d/