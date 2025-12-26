import React, { useState } from "react";
import axios from "axios";
import "../styles/Login.css";

function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await axios.post("http://127.0.0.1:5000/login", {
        email,
        password,
      });

      if (res.data.success) {
        onLogin();
      }
    } catch {
      setError("Invalid email or password");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">Login</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <p>
        Demo login:<br />
        <b>admin@example.com</b> / <b>admin123</b>
      </p>
    </div>
  );
}

export default Login;
