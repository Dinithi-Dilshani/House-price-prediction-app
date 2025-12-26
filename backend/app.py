from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# ---------------- LOAD MODEL ----------------
with open("models/best_house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------- LOGIN (NO JWT) ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Demo credentials
    if email == "admin@example.com" and password == "admin123":
        return jsonify({"success": True})

    return jsonify({"success": False, "message": "Invalid credentials"}), 401

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Convert Yes/No to 1/0
        def yes_no(val):
            return 1 if val == "Yes" else 0

        # Map categorical grades/conditions to numbers
        grade_map = {
            "Very Poor": 0,
            "Poor": 1,
            "Average": 2,
            "Good": 3,
            "Very Good": 4,
            "Excellent": 5
        }

        condition_map = {
            "Poor": 0,
            "Fair": 1,
            "Good": 2,
            "Very Good": 3,
            "Excellent": 4
        }

        # Build features array (10 features)
        features = [
            float(data["area"]),               # Living area
            int(data["bedrooms"]),             # Bedrooms
            int(data["bathrooms"]),            # Bathrooms
            int(data["floors"]),               # Floors
            int(data["year_built"]),           # Year built
            int(data["parking"]),              # Parking
            yes_no(data["waterfront"]),        # Waterfront
            yes_no(data["renovated"]),         # Renovated
            grade_map[data["grade"]],          # Grade
            condition_map[data["condition"]],  # Condition
        ]

        features = np.array(features).reshape(1, -1)

        # Scale and predict
        scaled_features = scaler.transform(features)
        price = model.predict(scaled_features)[0]

        return jsonify({"predicted_price": round(float(price), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
