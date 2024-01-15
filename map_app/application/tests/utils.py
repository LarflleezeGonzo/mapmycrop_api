from jose import jwt
from application.core.config import settings
from datetime import datetime, timedelta

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ISSUER = "your-issuer"

def create_test_jwt(subject: str = "", expires_in_minutes: int = 15) -> str:
    """
    Create a JWT token for testing purposes.

    Parameters:
        - subject: Subject of the token (e.g., user ID or username).
        - expires_in_minutes: Expiration time of the token in minutes.

    Returns:
        - str: JWT token.
    """
    expiration_time = datetime.utcnow() + timedelta(minutes=expires_in_minutes)

    token_data = {
        "sub": subject,
        "exp": expiration_time,
        "iss": ISSUER,
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    print(token)
    return token

def create_invalid_test_jwt(subject: str = "", expires_in_minutes: int = 15) -> str:
    """
    Create a JWT token for testing purposes.

    Parameters:
        - subject: Subject of the token (e.g., user ID or username).
        - expires_in_minutes: Expiration time of the token in minutes.

    Returns:
        - str: JWT token.
    """
    expiration_time = datetime.utcnow() + timedelta(minutes=expires_in_minutes)

    token_data = {
        "sub": subject,
        "exp": expiration_time,
        "iss": ISSUER,
    }

    token = jwt.encode(token_data, "jnsfjnn", algorithm=ALGORITHM)
    return token