
# UserBase - Django Project

UserBase is a Django project for user management with a RESTful API, including features like user registration, profile updates, token management, and more.

---

## Table of Contents
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Local Run](#local-run)
- [Run with Docker](#run-with-docker)
- [Run with Docker Compose](#run-with-docker-compose)
- [.env File](#env-file)
- [API Endpoints](#api-endpoints)

---

## System Requirements
- Python 3.8+
- Django 4.0+
- Gunicorn (for production)
- Docker & Docker Compose
- CORS Headers (for frontend integration)
- PostgreSQL or SQLite (your choice)

---

## Installation
1. Clone the project:
   ```bash
   git clone https://github.com/razmazlih/UserBase.git
   cd UserBase
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following structure:
   ```plaintext
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
   ```

4. Create the database migrations:
   ```bash
   python manage.py makemigrations
   ```

5. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

---

## Local Run
To run the local development server:
```bash
python manage.py runserver
```

The project will be available at:
```
http://127.0.0.1:8000
```

---

## Run with Docker
To run the project using Docker:

1. Build the Docker image:
   ```bash
   docker build -t userbase .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 --env-file .env userbase
   ```

3. The application will be accessible at:
   ```
   http://127.0.0.1:8000
   ```

---

## Run with Docker Compose
Alternatively, you can use `docker-compose` for easier setup:

1. Ensure the `docker-compose.yml` file is present in the project root.

2. Run the application using `docker-compose`:
   ```bash
   docker-compose up -d
   ```

3. Access the application at:
   ```
   http://127.0.0.1:8001
   ```

---

## .env File
The `.env` file is required to run the project. Example:
```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## API Endpoints
### User Registration
- **Endpoint**: `http://127.0.0.1:8000/api/users/register/`
- **Method**: `POST`
- **Body**:
    ```json
    {
        "username": "example",
        "password": "Password123",
        "phone_number": "0505050505",
        "city": "city name",
        "street_name": "street name",
        "house_number": 1
    }
    ```

### Update User Profile
- **Endpoint**: `http://127.0.0.1:8000/api/users/profile/`
- **Method**: `PUT`
- **Header**:
    ```
    Authorization: Bearer {jwt-token}
    Content-Type: application/json
    ```
- **Body**:
    ```json
    {
        "phone_number": "0505050505",
        "city": "city name update",
        "street_name": "street name update",
        "house_number": 2
    }
    ```

### Change Password
- **Endpoint**: `http://127.0.0.1:8000/api/users/change-password/`
- **Method**: `PUT`
- **Header**:
    ```
    Authorization: Bearer {jwt-token}
    Content-Type: application/json
    ```
- **Body**:
    ```json
    {
        "new_password": "Password123!"
    }
    ```

### Login and Get Token
- **Endpoint**: `http://127.0.0.1:8000/api/login/`
- **Method**: `POST`
- **Body**:
    ```json
    {
        "username": "example",
        "password": "Password123!"
    }
    ```

---

## Notes
- Ensure your database is properly configured in the `settings.py` file.
- Secure the SECRET_KEY in production.
- Use HTTPS in production environments.

---

Good luck!
