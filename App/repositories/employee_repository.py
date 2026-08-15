from App.utils.json_service import JsonService
from App.config.setting import Settings


class EmployeeRepository:

    @staticmethod
    def get_all():
        return JsonService.read_file(Settings.EMPLOYEE_FILE)

    @staticmethod
    def save_all(employees):
        JsonService.write_file(Settings.EMPLOYEE_FILE, employees)

    @staticmethod
    def get_by_id(employee_id: int):
        employees = EmployeeRepository.get_all()
        return next(
            (emp for emp in employees if emp["id"] == employee_id),
            None
        )

    @staticmethod
    def search_by_name(name: str):
        employees = EmployeeRepository.get_all()
        return [
            emp for emp in employees
            if name.lower() in emp["name"].lower()
        ]

    @staticmethod
    def get_next_id():
        employees = EmployeeRepository.get_all()
        return max((emp["id"] for emp in employees), default=0) + 1
    
    