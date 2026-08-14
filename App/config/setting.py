import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    USER_FILE = "Data/users.json"
    EMPLOYEE_FILE = "Data/employees.json"
    DEPARTMENT_FILE = "Data/departments.json"
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )


settings = Settings()