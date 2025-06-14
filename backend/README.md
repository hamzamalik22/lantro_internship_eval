# LantroTech Backend

This is the backend implementation for the LantroTech coding challenge, built with Django and Django REST Framework.

## Technologies Used

- Python 3.x
- Django 5.2.3
- Django REST Framework 3.16.0
- MySQL
- JWT Authentication
- CORS Headers

## Architecture

The backend follows a simple and clean architecture:
- Function-based views (FBV) for API endpoints
- JWT-based authentication
- MySQL database
- RESTful API design

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install django djangorestframework django-cors-headers mysqlclient bcrypt
```

3. Create a MySQL database named 'lantro_db'

4. Update database settings in `lantro_backend/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lantro_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'hamza',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `POST /api/signup/` - Register a new user
- `POST /api/login/` - Login and get JWT tokens
- `GET /api/dashboard/` - Get user dashboard data (requires authentication)
- `POST /api/logout/` - Logout and invalidate token

## Possible Improvements

1. Add more comprehensive input validation
2. Implement rate limiting
3. Add API documentation using Swagger/OpenAPI
4. Add unit tests
5. Implement refresh token rotation
6. Add more security features (password reset, email verification)
7. Add logging and monitoring
8. Implement caching for better performance 