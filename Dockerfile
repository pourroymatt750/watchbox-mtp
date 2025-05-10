# syntax=docker/dockerfile:1
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project
COPY . /code/

# Start the Django app with Gunicorn
CMD gunicorn watchbox_mtp.wsgi:application --bind 0.0.0.0:8000
