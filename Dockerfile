FROM python:3.9

WORKDIR /app_src/

COPY ./app_src/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app_src /app_src/

CMD ["uvicorn", "start_api:app", "--host", "0.0.0.0"]
