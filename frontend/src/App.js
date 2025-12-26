import React, { useState } from "react";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [page, setPage] = useState("dashboard");

  if (!isLoggedIn) {
    return <Login onLogin={() => setIsLoggedIn(true)} />;
  }

  if (page === "predict") {
    return <Predict onBack={() => setPage("dashboard")} />;
  }

  return (
    <Dashboard
      onNavigate={setPage}
      onLogout={() => setIsLoggedIn(false)}
    />
  );
}

export default App;
