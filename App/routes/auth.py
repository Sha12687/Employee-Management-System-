from fastapi import APIRouter, HTTPException
from App.models.auth import LoginRequest, TokenResponse
from App.services.auth_service import AuthService
from App.utils.security import create_access_token

router =APIRouter()

@router.post("/login",response_model=TokenResponse)
def login(user_data:LoginRequest):
    user = AuthService.authenticate_user(
        user_data.username,
        user_data.password
        )
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    token= create_access_token({"sub":user["username"],"employee_id": user["id"],"role":user["role"]})
    return {
        "access_token": token,
        "token_type": "bearer"
    }    
    