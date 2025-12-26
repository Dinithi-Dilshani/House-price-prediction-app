import React, { useState } from "react";
import axios from "axios";
import "../styles/Predict.css";

function Predict({ onBack }) {
  const [formData, setFormData] = useState({
    area: 1200,
    bedrooms: 3,
    bathrooms: 2,
    floors: 1,
    year_built: 2010,
    parking: 1,
    grade: "Average",
    condition: "Good",
    waterfront: "No",
    renovated: "No",
  });

  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const predictPrice = async () => {
    setLoading(true);
    setPrice(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.data.predicted_price) {
        setPrice(response.data.predicted_price);
      }
    } catch (error) {
      console.error(error);
      alert(
        "Prediction failed. Make sure backend is running and all inputs are correct."
      );
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <button className="back-btn" onClick={onBack}>
        ← Back to Dashboard
      </button>

      <h1>🏠 House Price Prediction</h1>

      <h2>🏡 Property Details</h2>
      <div className="form-grid">
        <div className="form-group">
          <label>Living Area (sq ft)</label>
          <input
            type="number"
            name="area"
            value={formData.area}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Bedrooms</label>
          <input
            type="number"
            name="bedrooms"
            value={formData.bedrooms}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Bathrooms</label>
          <input
            type="number"
            name="bathrooms"
            value={formData.bathrooms}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Floors</label>
          <input
            type="number"
            name="floors"
            value={formData.floors}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Year Built</label>
          <input
            type="number"
            name="year_built"
            value={formData.year_built}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Parking Spaces</label>
          <input
            type="number"
            name="parking"
            value={formData.parking}
            onChange={handleChange}
          />
        </div>
      </div>

      <h2>⭐ House Quality</h2>
      <div className="form-grid">
        <div className="form-group">
          <label>Overall Grade</label>
          <select
            name="grade"
            value={formData.grade}
            onChange={handleChange}
          >
            <option>Very Poor</option>
            <option>Poor</option>
            <option>Average</option>
            <option>Good</option>
            <option>Very Good</option>
            <option>Excellent</option>
          </select>
        </div>

        <div className="form-group">
          <label>Condition</label>
          <select
            name="condition"
            value={formData.condition}
            onChange={handleChange}
          >
            <option>Poor</option>
            <option>Fair</option>
            <option>Good</option>
            <option>Very Good</option>
            <option>Excellent</option>
          </select>
        </div>

        <div className="form-group">
          <label>Waterfront</label>
          <select
            name="waterfront"
            value={formData.waterfront}
            onChange={handleChange}
          >
            <option>No</option>
            <option>Yes</option>
          </select>
        </div>

        <div className="form-group">
          <label>Renovated</label>
          <select
            name="renovated"
            value={formData.renovated}
            onChange={handleChange}
          >
            <option>No</option>
            <option>Yes</option>
          </select>
        </div>
      </div>

      <button
        className="predict-btn"
        onClick={predictPrice}
        disabled={loading}
      >
        {loading ? "Predicting..." : "Predict Price"}
      </button>

      {price && (
        <h2 className="result">
          Estimated Price: ${price.toLocaleString()}
        </h2>
      )}
    </div>
  );
}

export default Predict;
