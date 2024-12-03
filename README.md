
# UserBase - Django Project

UserBase is a Django project for user management with a RESTful API, including features like user registration, profile updates, token management, and more.

---

## Table of Contents
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Local Run](#local-run)
- [Run with Gunicorn](#run-with-gunicorn)
- [.env File](#env-file)
- [API Endpoints](#api-endpoints)

---

## System Requirements
- Python 3.8+
- Django 4.0+
- Gunicorn (for production)
- CORS Headers (for frontend integration)
- MySQL/PostgreSQL or SQLite (your choice)

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

## Run with Gunicorn
To run in production mode using Gunicorn:
```bash
gunicorn user_base.wsgi:application --bind 0.0.0.0:8000 --daemon
```

---

## .env File
The `.env` file is required to run the project. Example:
```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
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
