FROM python:3.11
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY app/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . .

EXPOSE 8080