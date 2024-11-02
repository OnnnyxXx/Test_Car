FROM python:3.12

RUN mkdir /car

WORKDIR /car

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean
#
# COPY wait-for-it.sh /usr/local/bin/wait-for-it
# RUN chmod +x /usr/local/bin/wait-for-it
#
# EXPOSE 8000

CMD ["bash", "wait-for-it.sh", "postgres", "5432", "--", "bash", "-c", "gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

