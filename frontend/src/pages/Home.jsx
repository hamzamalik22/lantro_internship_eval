import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="home-container">
      <div className="home-content">
        <div className="home-header">
          <h1>LantroTech</h1>
          <p>HR Management System</p>
        </div>
        <div className="home-description">
          <p>Welcome to LantroTech's HR Management System. Streamline your HR processes with our comprehensive solution.</p>
        </div>
        <div className="home-actions">
          <Link to="/signup" className="home-button signup-button">
            Create Account
          </Link>
          <Link to="/login" className="home-button login-button">
            Sign In
          </Link>
        </div>
      </div>
    </div>
  );
} 