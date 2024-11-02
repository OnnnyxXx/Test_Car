FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY wait-for-it.sh /app/

# Открываем порт для доступа
EXPOSE 8000

CMD ["bash", "wait-for-it.sh", "postgres", "5432", "--", "bash", "-c", "gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

