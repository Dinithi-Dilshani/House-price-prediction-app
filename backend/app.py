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

# ---------------- LOGIN ----------------
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

        # Build the full 20-feature input
        # Order MUST match the training data
        features = [
            int(data.get("bedrooms", 0)),                 # 1. number of bedrooms
            int(data.get("bathrooms", 0)),                # 2. number of bathrooms
            float(data.get("area", 0)),                   # 3. living area
            0,                                            # 4. lot area (dummy)
            int(data.get("floors", 0)),                   # 5. number of floors
            yes_no(data.get("waterfront", "No")),         # 6. waterfront present
            0,                                            # 7. number of views (dummy)
            data.get("condition_map", 2),                 # 8. condition of the house
            0,                                            # 9. grade of the house (ignored)
            0,                                            # 10. Area of the house(excluding basement) (dummy)
            0,                                            # 11. Area of the basement (dummy)
            int(data.get("yearBuilt", 0)),                # 12. Built Year
            yes_no(data.get("renovated", "No")),          # 13. Renovation Year (Yes/No mapped to 0/1)
            0,                                            # 14. Postal Code (dummy)
            0,                                            # 15. Latitude (dummy)
            0,                                            # 16. Longitude (dummy)
            0,                                            # 17. living_area_renov (dummy)
            0,                                            # 18. lot_area_renov (dummy)
            0,                                            # 19. Number of schools nearby (dummy)
            0                                             # 20. Distance from airport (dummy)
        ]

        features_array = np.array(features).reshape(1, -1)

        # Scale and predict
        scaled_features = scaler.transform(features_array)
        price = model.predict(scaled_features)[0]

        return jsonify({"predicted_price": round(float(price), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
