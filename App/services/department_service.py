from App.utils.json_service import JsonService 
from App.models.department import CreateDepartment ,CreateDepartmentUpdate,DepartmentResponse 
from App.config.setting import Settings
from App.repositories.department_repository import Department_repository

class DepartmentService:
    @staticmethod
    def get_all_department():
        return Department_repository.get_all()
    
    @staticmethod
    def add_department(Data:CreateDepartment):
        depts =Department_repository.get_all()
        new_dept ={
            "id": Department_repository.get_next_id(),
            "deptName":Data.deptName,
            "deptLocation":Data.deptLocation
        }
        
        depts.append(new_dept)
        Department_repository.save_all(depts)
        return new_dept
    @staticmethod
    def delete_department(id):
        depts =Department_repository.get_all()
        _dept=next((dept for dept in depts if dept["id"]==id),None)
        if _dept is None:
            return None
        depts.remove(_dept)
        Department_repository.save_all(depts)
        return _dept
    
      
    @staticmethod
    def update_department(id,dept:CreateDepartmentUpdate):
        depts =Department_repository.get_all()
        _dept=next((dept for dept in depts if dept["id"]==id),None)
        if _dept is None:
            return None
        _dept["deptName"]=dept.deptName
        _dept["deptLocation"]=dept.deptLocation
        Department_repository.save_all(depts)
        return _dept
    @staticmethod 
    def get_department_by_id(id):
        data=Department_repository.get_all()
        _dept=next((dept for dept in data if dept["id"]==id),None)
        if _dept is None:
            return None
        return _dept
    
    @staticmethod 
    def get_department_by_city(city):
        return Department_repository.get_by_city(city)
        