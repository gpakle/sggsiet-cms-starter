FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app

# ensure instance and media folder exists
RUN mkdir -p /app/instance/media

ENV FLASK_APP=manage.py
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "manage:app", "--workers", "3", "--threads", "4"]
