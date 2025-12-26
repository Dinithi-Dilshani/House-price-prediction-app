// src/auth.js

// Save token to localStorage
export const setToken = (token) => {
  localStorage.setItem("token", token);
};

// Get token from localStorage
export const getToken = () => {
  return localStorage.getItem("token");
};

// Remove token
export const logout = () => {
  localStorage.removeItem("token");
};
