import React from "react";
import { logout } from "../auth";
import "../styles/Dashboard.css";


function Dashboard({ onNavigate, onLogout }) {
  return (
    <div className="dashboard-container">
      <div className="dashboard-card">
        <h1>🏠 House Price Predictor</h1>
        <p className="dashboard-text">
          Welcome! This application helps you estimate house prices based on
          property details and house quality factors.
        </p>

        <div className="dashboard-actions">
          <button onClick={() => onNavigate("predict")}>
            Go to Prediction
          </button>

          <button className="logout-btn" onClick={() => {
            logout();
            onLogout();
          }}>
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
