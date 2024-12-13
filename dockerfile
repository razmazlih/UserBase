FROM python:3.12.4

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "0.0.0.0:8000", "user_base.wsgi:application"]