from typing import Optional

from App.utils.json_service import JsonService
from App.config.setting import Settings


class UserRepository:
    """
    Handles reading and retrieving users from the data source.
    """

    @staticmethod
    def get_all_users() -> list[dict]:
        return JsonService.read_file(Settings.USER_FILE)

    @staticmethod
    def get_user_by_username(username: str) -> Optional[dict]:
        users = UserRepository.get_all_users()

        for user in users:
            if user["username"] == username:
                return user

        return None