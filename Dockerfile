FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app .

ARG APP_VERSION=local
ENV APP_VERSION=$APP_VERSION

CMD ["python", "app.py"]