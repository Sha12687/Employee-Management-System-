import os
from App.config.setting import settings
from fastapi import HTTPException,FastAPI,Depends
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from App.utils.security import decode_access_token
# We don't want to manually read the Authorization header in every endpoint.
# It automatically extracts: Authorization: Bearer eyJ...
# FastAPI, whenever I ask for a token, get it from the Authorization Bearer header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Depends This connects directly to what you learned earlier about FastAPI Dependency Injection.
 
def get_current_user(token:str =Depends(oauth2_scheme)):
    payload=decode_access_token(token)
    if payload is None:
        raise  HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    return payload


def require_admin(current_user:dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return current_user 
# Header

# +

# Payload

# +

# SECRET_KEY

# ↓

# HS256

# ↓

# JWT