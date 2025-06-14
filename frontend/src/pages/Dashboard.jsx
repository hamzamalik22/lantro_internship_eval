import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';

export default function Dashboard() {
  const { user, logout } = useAuth();
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    const fetchDashboardData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/dashboard/');
        setDashboardData(response.data);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, [user, navigate]);

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <nav className="dashboard-nav">
        <div className="nav-content">
          <div className="nav-left">
            <h1>LantroTech</h1>
          </div>
          <div className="nav-right">
            <div className="user-info">
              <span className="user-name">{user?.first_name} {user?.last_name}</span>
              <span className="user-role">{user?.role}</span>
            </div>
            <button onClick={handleLogout} className="logout-button">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                <polyline points="16 17 21 12 16 7" />
                <line x1="21" y1="12" x2="9" y2="12" />
              </svg>
              Logout
            </button>
          </div>
        </div>
      </nav>

      <main className="dashboard-main">
        <div className="dashboard-header">
          <h2>Welcome back, {user?.first_name}!</h2>
          <p>Here's what's happening in your dashboard.</p>
        </div>

        <div className="dashboard-grid">
          {dashboardData?.widgets && Object.entries(dashboardData.widgets).map(([key, value]) => (
            <div key={key} className="dashboard-card">
              <div className="card-header">
                <h3>{key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}</h3>
              </div>
              <div className="card-content">
                <div className="stat-value">{value}</div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
} 