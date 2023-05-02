FROM python:3.11-slim-buster

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api_distance_public_transportation /code/api_distance_public_transportation

CMD ["uvicorn", "api_distance_public_transportation.main:app", "--host", "0.0.0.0", "--port", "8080"]