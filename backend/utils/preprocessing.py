def build_full_input(user):
    """
    user: dictionary coming from frontend (React)
    Returns: full feature dictionary with 20 features
    """

    full = {}

    # -------- User-provided inputs (with safe defaults) --------
    full['number of bedrooms'] = user.get('bedrooms', 3)
    full['number of bathrooms'] = user.get('bathrooms', 2)
    full['living area'] = user.get('livingArea', 1200)
    full['lot area'] = user.get('lotArea', 4000)
    full['number of floors'] = user.get('floors', 1)
    full['waterfront present'] = user.get('waterfront', 0)
    full['condition of the house'] = user.get('condition', 3)
    full['grade of the house'] = user.get('grade', 7)
    full['Built Year'] = user.get('builtYear', 2000)
    full['Postal Code'] = user.get('postalCode', 98103)

    # -------- Auto-filled / derived features --------
    full['number of views'] = user.get('views', 0)

    full['Area of the house(excluding basement)'] = user.get('livingArea', 1200)
    full['Area of the basement'] = user.get('basementArea', 0)

    # If not renovated, assume same as built year
    full['Renovation Year'] = user.get('renovationYear', full['Built Year'])

    # Fixed / average location values (Seattle dataset assumption)
    full['Lattitude'] = 47.65
    full['Longitude'] = -122.35

    full['living_area_renov'] = user.get('livingArea', 1200)
    full['lot_area_renov'] = user.get('lotArea', 4000)

    full['Number of schools nearby'] = user.get('schoolsNearby', 3)
    full['Distance from the airport'] = user.get('distanceAirport', 25)

    return full
