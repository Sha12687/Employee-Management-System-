from typing import Optional

from App.repositories.user_repository import UserRepository
from App.utils.security import verify_password


class AuthService:
    """
    Handles user authentication and credential verification.
    """

    @staticmethod
    def authenticate_user(
        username: str,
        password: str
    ) -> Optional[dict]:
        user = UserRepository.get_user_by_username(username)
        if user is None:
            return None
        if verify_password(password, user["password_hash"]):
            return user
        return None