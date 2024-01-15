from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from application.core.config import settings

# Define a secret key for JWT
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# OAuth2 scheme with Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency to validate the token
async def validate_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception