from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from utils.preprocessing import build_full_input

app = Flask(__name__)
CORS(app)

# -----------------------------
# Load model and scaler
# -----------------------------
with open("models/best_house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# -----------------------------
# Feature order (MUST match training)
# -----------------------------
FEATURE_COLUMNS = [
    'number of bedrooms',
    'number of bathrooms',
    'living area',
    'lot area',
    'number of floors',
    'waterfront present',
    'number of views',
    'condition of the house',
    'grade of the house',
    'Area of the house(excluding basement)',
    'Area of the basement',
    'Built Year',
    'Renovation Year',
    'Postal Code',
    'Lattitude',
    'Longitude',
    'living_area_renov',
    'lot_area_renov',
    'Number of schools nearby',
    'Distance from the airport'
]

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json   # data from React frontend

    # Build full 20-feature input
    full_input = build_full_input(data)

    # Convert to ordered list
    features = [full_input[col] for col in FEATURE_COLUMNS]

    # Scale and predict
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)[0]

    return jsonify({
        "predicted_price": round(float(prediction), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
