from App.models.employee import CreateEmployee
from App.repositories.employee_repository import EmployeeRepository


class EmployeeService:

    @staticmethod
    def add_employee(employee: CreateEmployee):

        employees = EmployeeRepository.get_all()

        new_employee = {
            "id": EmployeeRepository.get_next_id(),
            "name": employee.name,
            "age": employee.age,
            "city": employee.city,
            "country": employee.country
        }

        employees.append(new_employee)

        EmployeeRepository.save_all(employees)

        return new_employee
    
    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all()

    @staticmethod
    def get_employee_by_id(employee_id: int):
        return EmployeeRepository.get_by_id(employee_id)
    
    @staticmethod
    def update_employee(employee_id: int, updated_employee: CreateEmployee):
    
        employees = EmployeeRepository.get_all()
    
        employee = next(
            (emp for emp in employees if emp["id"] == employee_id),
            None
        )
    
        if employee is None:
            return None
    
        employee["name"] = updated_employee.name
        employee["age"] = updated_employee.age
        employee["city"] = updated_employee.city
        employee["country"] = updated_employee.country
    
        EmployeeRepository.save_all(employees)
    
        return employee
    
    @staticmethod
    def delete_employee(employee_id: int):
    
        employees = EmployeeRepository.get_all()
    
        employee = next(
            (emp for emp in employees if emp["id"] == employee_id),
            None
        )
    
        if employee is None:
            return None
    
        employees.remove(employee)
    
        EmployeeRepository.save_all(employees)
    
        return employee
    
    @staticmethod
    def search_employee(name: str):
        return EmployeeRepository.search_by_name(name)