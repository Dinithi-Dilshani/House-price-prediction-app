import React, { useState, useEffect } from "react";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";

import { getToken, logout } from "./auth";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState("dashboard");

  useEffect(() => {
    const token = getToken();
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLogin = () => {
    setIsLoggedIn(true);
    setCurrentPage("dashboard");
  };

  const handleLogout = () => {
    logout();
    setIsLoggedIn(false);
    setCurrentPage("dashboard");
  };

  const handleNavigate = (page) => {
    setCurrentPage(page);
  };

  if (!isLoggedIn) {
    return <Login onLogin={handleLogin} />;
  }

  if (currentPage === "predict") {
    return <Predict onBack={() => setCurrentPage("dashboard")} />;
  }

  return (
    <Dashboard
      onNavigate={handleNavigate}
      onLogout={handleLogout}
    />
  );
}

export default App;
