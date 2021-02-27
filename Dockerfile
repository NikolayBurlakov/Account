FROM python:3.8

ENV PYTHONUNBUFFERED=1
COPY ./code ./code
WORKDIR /code
RUN pip install -U pip==21.0.1
RUN pip install -r requirements.txt
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]

