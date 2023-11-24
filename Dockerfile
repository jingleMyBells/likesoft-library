FROM python:3.11
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY library/ .
COPY ./deploy/server-entrypoint.sh ./entrypoints/server-entrypoint.sh
COPY ./deploy/worker-entrypoint.sh ./entrypoints/worker-entrypoint.sh

RUN chmod +x /app/entrypoints/server-entrypoint.sh
RUN chmod +x /app/entrypoints/worker-entrypoint.sh