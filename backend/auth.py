import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# ---------------- CONFIG ----------------
SECRET_KEY = "secret123"
JWT_ALGORITHM = "HS256"
JWT_EXP_HOURS = 1

# ---------------- DEMO USER ----------------
# Password is "admin123"
USER = {
    "email": "admin@example.com",
    "password": generate_password_hash("admin123")
}

# ---------------- LOGIN FUNCTION ----------------
def login_user(email, password):
    """
    Validates user credentials and returns JWT token if valid
    """
    if email == USER["email"] and check_password_hash(USER["password"], password):
        token = jwt.encode(
            {
                "email": email,
                "exp": datetime.utcnow() + timedelta(hours=JWT_EXP_HOURS)
            },
            SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )
        return token

    return None


# ---------------- TOKEN VERIFY (optional) ----------------
def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
