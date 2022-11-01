FROM python:3.8.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./test_app /code/test_app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]