from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

from auth import login_user   # ✅ USE auth.py

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

    token = login_user(email, password)

    if token:
        return jsonify({
            "success": True,
            "token": token
        }), 200

    return jsonify({
        "success": False,
        "message": "Invalid credentials"
    }), 401


# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        def yes_no(value):
            return 1 if value == "Yes" else 0

        features = [
            float(data["area"]),
            int(data["bedrooms"]),
            int(data["bathrooms"]),
            int(data["stories"]),
            yes_no(data["mainroad"]),
            yes_no(data["guestroom"]),
            yes_no(data["basement"]),
            yes_no(data["hotwaterheating"]),
            yes_no(data["airconditioning"]),
            int(data["parking"]),
            yes_no(data["prefarea"]),
        ]

        features_array = np.array(features).reshape(1, -1)

        scaled_features = scaler.transform(features_array)
        prediction = model.predict(scaled_features)[0]

        return jsonify({
            "prediction": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
