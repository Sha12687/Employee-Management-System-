from App.models.employee import CreateEmployee
from App.utils.json_service import JsonService 
from App.config.setting import Settings

class EmployeeService:
    @staticmethod
    def add_employee(employee:CreateEmployee):
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        new_employee={
           "id": max((emp["id"] for emp in data), default=0) + 1,
           "name": employee.name,
           "age": employee.age,
           "city": employee.city,
           "country": employee.country
        } 
        data.append(new_employee)
        JsonService.write_file(Settings.EMPLOYEE_FILE,data)
        return new_employee
    
    @staticmethod
    def get_all_employees():
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        return data
    @staticmethod
    def get_employee_by_id(id):
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        _empById=next((emp for emp in data if emp["id"]==id),None)
        return _empById
    @staticmethod
    def update_employee(id,updated_employee:CreateEmployee):
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        _empById=next((emp for emp in data if emp["id"]==id),None)
        if _empById is None:
            return None
        _empById["name"]=updated_employee.name
        _empById["age"] = updated_employee.age
        _empById["city"] = updated_employee.city
        _empById["country"] = updated_employee.country
        JsonService.write_file(Settings.EMPLOYEE_FILE,data)
        return _empById
            
    @staticmethod 
    def delete_employee(id:int):
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        _empById=next((emp for emp in data if emp["id"]==id),None)
        if _empById is None:
            return None
        data.remove(_empById)
        JsonService.write_file(Settings.EMPLOYEE_FILE,data)
        return _empById
    @staticmethod   
    def search_employee(name):
        data=JsonService.read_file(Settings.EMPLOYEE_FILE)
        return [emp for emp in data if name.lower() in emp["name"].lower()]
        