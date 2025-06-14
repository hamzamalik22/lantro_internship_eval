# LantroTech HR Management System

A full-stack web application for HR management, built with Django and React.

## Technologies Used

### Backend
- Django 4.2
- Django REST Framework
- MySQL
- JWT Authentication
- Django CORS Headers

### Frontend
- React 18
- React Router DOM
- Axios
- Custom CSS

## Architecture

The application follows a modern client-server architecture:

### Backend Architecture
- Django REST Framework for API endpoints
- JWT-based authentication
- MySQL database for data persistence
- Custom user model with role-based access control

### Frontend Architecture
- React components for UI
- Context API for state management
- Protected routes for authenticated access
- Responsive design using CSS Grid and Flexbox

## Features

- User authentication (signup, login, logout)
- Role-based access control (SUPER ADMIN, ADMIN)
- Dashboard with role-specific widgets
- Responsive design
- Form validation (frontend and backend)
- Secure password hashing
- Protected API endpoints

## Setup and Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- MySQL 8.0+

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure MySQL database:
   - Create a new database
   - Update settings.py with database credentials

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

- `POST /api/signup/` - User registration
- `POST /api/login/` - User authentication
- `GET /api/dashboard/` - Dashboard data
- `POST /api/logout/` - User logout

## Possible Improvements

1. **Authentication**
   - Implement refresh token mechanism
   - Add session expiration handling
   - Add password reset functionality

2. **Documentation**
   - Add Swagger/OpenAPI documentation
   - Improve code documentation
   - Add API usage examples

3. **Features**
   - Add user profile management
   - Implement email verification
   - Add more dashboard widgets
   - Add data export functionality

4. **Security**
   - Add rate limiting
   - Implement 2FA
   - Add audit logging

5. **Testing**
   - Add unit tests
   - Add integration tests
   - Add end-to-end tests

## License

This project is licensed under the MIT License. 