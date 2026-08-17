from App.services.auth_service import AuthService
from fastapi.testclient import TestClient

user =AuthService.authenticate_user(
    "admin","SHA1234"
)



user1 =AuthService.authenticate_user(
    "employee","worng"
)



