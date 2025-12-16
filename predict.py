import pickle
import pandas as pd

# --------------------
# Load model and scaler
# --------------------
with open("best_house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --------------------
# Feature order used in training
# --------------------
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

# --------------------
# Prediction function
# --------------------
def predict_price(input_dict):
    """
    input_dict: dictionary with keys = FEATURE_COLUMNS
    Returns: predicted house price
    """
    # Check for missing features
    missing_features = [col for col in FEATURE_COLUMNS if col not in input_dict]
    if missing_features:
        raise ValueError(f"Missing feature(s): {missing_features}")

    # Convert dict to DataFrame (1 row) with correct column order
    df = pd.DataFrame([input_dict], columns=FEATURE_COLUMNS)

    # Scale the input
    scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(scaled)[0]
    return prediction

# --------------------
# Example usage
# --------------------
if __name__ == "__main__":
    example_input = {
        'number of bedrooms': 3,
        'number of bathrooms': 2,
        'living area': 1800,
        'lot area': 5000,
        'number of floors': 2,
        'waterfront present': 0,
        'number of views': 3,
        'condition of the house': 4,
        'grade of the house': 8,
        'Area of the house(excluding basement)': 1500,
        'Area of the basement': 300,
        'Built Year': 2005,
        'Renovation Year': 2015,
        'Postal Code': 98103,
        'Lattitude': 47.65,
        'Longitude': -122.35,
        'living_area_renov': 1800,
        'lot_area_renov': 5000,
        'Number of schools nearby': 4,
        'Distance from the airport': 25
    }

    predicted_price = predict_price(example_input)
    print("Predicted House Price:", predicted_price)
