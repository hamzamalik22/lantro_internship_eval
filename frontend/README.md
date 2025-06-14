# LantroTech Frontend

This is the frontend implementation for the LantroTech coding challenge, built with React and Tailwind CSS.

## Technologies Used

- React 19
- React Router DOM
- Tailwind CSS
- Axios
- Headless UI
- Heroicons

## Features

- User authentication (login/signup)
- Protected routes
- Role-based dashboard
- Responsive design
- JWT token management

## Setup Instructions

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## Project Structure

- `src/components/auth/` - Authentication components (Login, Signup)
- `src/context/` - Context providers (AuthContext)
- `src/pages/` - Page components (Dashboard)
- `src/App.jsx` - Main application component with routing
- `src/main.jsx` - Application entry point

## API Integration

The frontend integrates with the following backend endpoints:

- POST /api/signup/ - Register a new user
- POST /api/login/ - Login and get JWT tokens
- GET /api/dashboard/ - Get user dashboard data
- POST /api/logout/ - Logout and invalidate token

## Possible Improvements

1. Add form validation
2. Implement error boundaries
3. Add loading states and error handling
4. Implement refresh token rotation
5. Add unit tests
6. Add more interactive widgets
7. Implement dark mode
8. Add user profile management
