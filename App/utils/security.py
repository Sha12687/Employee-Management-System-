import bcrypt
import os
from App.config.setting import settings
from fastapi import HTTPException,FastAPI,Depends
from jose import jwt,JWTError
from datetime import datetime , timedelta ,timezone

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
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    # Now the payload becomes:
    # {"sub": "admin","role": "admin","exp": datetime(...)}
    payload["exp"] = expire
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return token



def decode_access_token(token:str) -> dict|None:
    try:
        payload=jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None
