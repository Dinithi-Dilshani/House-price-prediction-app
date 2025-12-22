import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    livingArea: 1200,
    lotArea: 4000,
    bedrooms: 3,
    bathrooms: 2,
    floors: 1,
    builtYear: 2000,
    grade: "Average",
    condition: "Good",
    schoolsNearby: 3,
    distanceAirport: 25,
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
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        {
          ...formData,
          livingArea: Number(formData.livingArea),
          lotArea: Number(formData.lotArea),
          bedrooms: Number(formData.bedrooms),
          bathrooms: Number(formData.bathrooms),
          floors: Number(formData.floors),
          builtYear: Number(formData.builtYear),
          schoolsNearby: Number(formData.schoolsNearby),
          distanceAirport: Number(formData.distanceAirport),
        }
      );
      setPrice(response.data.predicted_price);
    } catch (error) {
      alert("Prediction failed. Is Flask backend running?");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🏠 House Price Prediction</h1>

      {/* Property Details */}
      <div className="card">
        <h2>🏘 Property Details</h2>

        <div className="field">
          <label>Living Area (sq ft)</label>
          <input name="livingArea" type="number" value={formData.livingArea} onChange={handleChange} />
        </div>

        <div className="field">
          <label>Lot Area (sq ft)</label>
          <input name="lotArea" type="number" value={formData.lotArea} onChange={handleChange} />
        </div>

        <div className="field">
          <label>Bedrooms</label>
          <input name="bedrooms" type="number" value={formData.bedrooms} onChange={handleChange} />
        </div>

        <div className="field">
          <label>Bathrooms</label>
          <input name="bathrooms" type="number" value={formData.bathrooms} onChange={handleChange} />
        </div>

        <div className="field">
          <label>Floors</label>
          <input name="floors" type="number" value={formData.floors} onChange={handleChange} />
        </div>

        <div className="field">
          <label>Built Year</label>
          <input name="builtYear" type="number" value={formData.builtYear} onChange={handleChange} />
        </div>
      </div>

      {/* House Quality */}
      <div className="card">
        <h2>⭐ House Quality</h2>

        <div className="field">
          <label>Overall Quality</label>
          <select name="grade" value={formData.grade} onChange={handleChange}>
            <option value="Poor">Poor</option>
            <option value="Below Average">Below Average</option>
            <option value="Average">Average</option>
            <option value="Good">Good</option>
            <option value="Excellent">Excellent</option>
          </select>
        </div>

        <div className="field">
          <label>House Condition</label>
          <select name="condition" value={formData.condition} onChange={handleChange}>
            <option value="Bad">Bad</option>
            <option value="Fair">Fair</option>
            <option value="Good">Good</option>
            <option value="Very Good">Very Good</option>
            <option value="Excellent">Excellent</option>
          </select>
        </div>

        <div className="field">
          <label>Schools Nearby</label>
          <input
            name="schoolsNearby"
            type="number"
            value={formData.schoolsNearby}
            onChange={handleChange}
          />
        </div>

        <div className="field">
          <label>Distance to Airport (km)</label>
          <input
            name="distanceAirport"
            type="number"
            value={formData.distanceAirport}
            onChange={handleChange}
          />
        </div>
      </div>

      <button onClick={predictPrice} disabled={loading}>
        {loading ? "Predicting..." : "Predict Price"}
      </button>

      {price && (
        <div className="result">
          Estimated Price: ${price.toLocaleString()}
        </div>
      )}
    </div>
  );
}

export default App;
