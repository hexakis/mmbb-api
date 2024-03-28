FROM python:3.11

# Setting work directory
COPY ./ /api
WORKDIR /api

ENV PROJECT_STATUS="DEV"

# Initalizing environment variables for configuration
ENV PROJECT_NAME="Marine Money Banking"
ENV PROJECT_VERSION=3.0
ENV DATABASE_URL='postgres:///admin:admin'
ENV NOOB_TOKEN="06cc603c-2da8-45a8-8f43-16b460207a50"

# Dev environment variables for configuration
ENV DEV_NAME="Marine Money Banking"
ENV DEV_VERSION=1.0
ENV DEV_DATABASE_URL="sqlite:///./bank.db"


# Installing python packages
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt


# Running FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

