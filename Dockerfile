FROM python:3.11
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY library/ .
CMD ["gunicorn", "library.wsgi:application", "--bind", "0:8000" ]