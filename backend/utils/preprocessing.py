# backend/utils/preprocessing.py

def build_full_input(user):
    """
    user: dictionary coming from React frontend (10 inputs)
    Returns: full feature dictionary with 20 features
    """

    full = {}

    # ===============================
    # USER INPUTS (10)
    # ===============================

    # Property details
    full['living area'] = user.get('livingArea', 1200)
    full['lot area'] = user.get('lotArea', 4000)

    full['number of bedrooms'] = user.get('bedrooms', 3)
    full['number of bathrooms'] = user.get('bathrooms', 2)
    full['number of floors'] = user.get('floors', 1)

    # House age & quality
    full['Built Year'] = user.get('builtYear', 2000)

    # Map UI quality (1–5) → dataset grade (1–13)
    quality_map = {
        1: 3,
        2: 5,
        3: 7,
        4: 10,
        5: 13
    }
    ui_quality = user.get('quality', 3)
    full['grade of the house'] = quality_map.get(ui_quality, 7)

    # Condition (1–5 fits dataset scale closely)
    full['condition of the house'] = user.get('condition', 3)

    # Location / environment
    full['waterfront present'] = user.get('waterfront', 0)
    full['number of views'] = user.get('views', 0)

    # ===============================
    # AUTO-FILLED FEATURES
    # ===============================

    full['Area of the house(excluding basement)'] = full['living area']
    full['Area of the basement'] = 0

    # Assume no renovation unless stated
    full['Renovation Year'] = full['Built Year']

    # Fixed / average location (Seattle dataset)
    full['Postal Code'] = 98103
    full['Lattitude'] = 47.65
    full['Longitude'] = -122.35

    # Renovated area assumed same as current
    full['living_area_renov'] = full['living area']
    full['lot_area_renov'] = full['lot area']

    # Neighborhood averages
    full['Number of schools nearby'] = 3
    full['Distance from the airport'] = 25

    return full
