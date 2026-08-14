from App.utils.json_service import JsonService 
from App.models.department import CreateDepartment ,CreateDepartmentUpdate,DepartmentResponse 
from App.config.setting import Settings

class DepartmentService:
    @staticmethod
    def get_all_department():
        data =JsonService.read_file(Settings.DEPARTMENT_FILE)
        return data
    
    @staticmethod
    def add_department(newData):
        data=JsonService.read_file(Settings.DEPARTMENT_FILE)
        _newdept={
            "id":max((emp["id"] for emp in data), default=0) + 1,
            "deptName":newData.deptName,
            "deptLocation":newData.deptLocation
        }
        data.append(_newdept)
        JsonService.write_file(Settings.DEPARTMENT_FILE,data)
        return _newdept
    
    @staticmethod
    def delete_department(id):
        data=JsonService.read_file(Settings.DEPARTMENT_FILE)
        _dept=next((dept for dept in data if dept["id"]==id),None)
        if _dept is None:
            return None
        data.remove(_dept)
        JsonService.write_file(Settings.DEPARTMENT_FILE,data)
        return _dept
    
      
    @staticmethod
    def update_department(id,dept:CreateDepartmentUpdate):
        data=JsonService.read_file(Settings.DEPARTMENT_FILE)
        _dept=next((dept for dept in data if dept["id"]==id),None)
        if _dept is None:
            return None
        _dept["deptName"]=dept.deptName
        _dept["deptLocation"]=dept.deptLocation
        JsonService.write_file(Settings.DEPARTMENT_FILE,data)
        return _dept
    @staticmethod 
    def get_department_by_id(id):
        data=JsonService.read_file(Settings.DEPARTMENT_FILE)
        _dept=next((dept for dept in data if dept["id"]==id),None)
        if _dept is None:
            return None
        return _dept
    
    @staticmethod 
    def get_department_by_city(city):
        data=JsonService.read_file(Settings.DEPARTMENT_FILE)
        return [dept for dept in data if city.lower() in dept["deptLocation"].lower() ]