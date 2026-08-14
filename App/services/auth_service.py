from App.utils.json_service import JsonService 
from App.utils.security import verify_password
from App.config.setting import Settings
from typing import Optional
class AuthService:
    """
    Handles user authentication and credential verification.
    """
    @staticmethod
    def authenticate_user(username:str, password:str)-> Optional[dict]:
        """
        Authenticate a user using username and password.
        Returns the user dictionary if successful, otherwise None.
        """
        users =JsonService.read_file(Settings.USER_FILE)
        for user in users:
            if user["username"]==username:
                if verify_password(password,user["password_hash"]):
                    return user
                return None   
        return None
    
    