FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ../../wait-for-it.sh /code/
COPY ../../requirements.txt /code/
RUN pip install --upgrade pip
COPY ../../ /code/
RUN chmod +x wait-for-it.sh && pip install -r requirements.txt