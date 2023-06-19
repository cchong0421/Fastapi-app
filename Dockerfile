FROM python:3.9

RUN mkdir -p /code/app
WORKDIR /code

COPY ./requirements.txt /code/
COPY ./app /code/app/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
