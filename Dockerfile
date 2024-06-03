FROM python:3.10

WORKDIR /code

COPY Pipfile /code/
RUN pip install --no-cache-dir pipenv && pipenv install --system --skip-lock

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
