import bcrypt
import os
from App.config import setting
from fastapi import HTTPException,FastAPI,Depends
from jose import jwt,JWTError
from datetime import datetime , timedelta ,timezone
from fastapi.security import OAuth2PasswordBearer
# We don't want to manually read the Authorization header in every endpoint.
# It automatically extracts: Authorization: Bearer eyJ...
# FastAPI, whenever I ask for a token, get it from the Authorization Bearer header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password:str)-> str:
    hashed_password= bcrypt.hashpw(
        # Convert the password from a Python string into bytes.
        password.encode("UTF-8"),
        # This generates a random salt.
        bcrypt.gensalt()
    )
    return hashed_password.decode("utf-8")

def verify_password(password:str,store_pass:str)->bool:
    return (bcrypt.checkpw(password.encode("UTF-8"),store_pass.encode("UTF-8")))

def create_access_token(data: dict) -> str:
    # Because we don't want to modify the original dictionary.
    payload = data.copy()
    print(f"PAYLOAD -: {payload}" )
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    print(f"EXPIRE TIME {expire}")
    # Now the payload becomes:
    # {"sub": "admin","role": "admin","exp": datetime(...)}
    payload["exp"] = expire

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    print(f"TOKEN RUNING -:{token}")
    return token



def decode_access_token(token:str) -> dict|None:
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None

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