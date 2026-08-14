from App.utils.json_service import JsonService 
from App.utils.security import verify_password
from App.config.setting import Settings
file_path_user="Data/users.json"
class AuthService:
    @staticmethod
    def authenticate_user(username, password):
        users =JsonService.read_file(Settings.USER_FILE)
        for user in users:
            if user["username"]==username:
                if verify_password(password,user["password_hash"]):
                    return user
                return None   
        return None
    
    