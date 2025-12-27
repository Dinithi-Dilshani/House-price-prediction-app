import React, { useState } from "react";
import axios from "axios";
import "../styles/Login.css";

function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://127.0.0.1:5000/login", {
        email,
        password,
      });

      if (res.data.success) {
        onLogin();
      }
    } catch (err) {
      setError("Invalid email or password");
    }
  };

  return (
  <div className="login-page">
    <div className="login-box">
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Login</button>
      </form>
      <h5>admin@example.com/admin123</h5>

      {error && <p className="error-text">{error}</p>}
    </div>
  </div>
);

}

export default Login;
