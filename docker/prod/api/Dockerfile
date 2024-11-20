FROM python:3.12.7-slim-bookworm

ENV PYTHONUNBUFFERED 1

COPY ../../../requirements.txt .

RUN pip install -r requirements.txt

COPY ../../../portfolio_backend .

EXPOSE 8000

WORKDIR /portfolio_backend

CMD ["gunicorn", "--env", "DJANGO_SETTINGS_MODULE=portfolio_backend.settings-prod", "portfolio_backend.wsgi:application", "--bind", "0.0.0.0:8000", "-c", "../../../config/gunicorn/prod.py"]
