FROM python:3.12.7-slim-bookworm

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "portfolio_backend/manage.py", "runserver", "0.0.0.0:8000"]
