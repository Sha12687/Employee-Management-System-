from App.utils.json_service import JsonService
from App.config.setting import Settings

class Department_repository:
    @staticmethod
    def get_all():
        return JsonService.read_file(Settings.DEPARTMENT_FILE)
    
    @staticmethod
    def get_by_id(id:int):
        depts = Department_repository.get_all()
        return next((dept for dept in depts if dept["id"]==id),None)
    
    @staticmethod
    def save_all(departments):
        JsonService.write_file(Settings.DEPARTMENT_FILE,departments)
    @staticmethod
    def search_by_name(name: str):
        depts = Department_repository.get_all()
        return [
            dept for dept in depts
            if name.lower() in dept["deptName"].lower()
        ]
        
    @staticmethod
    def get_by_city(city:str):
        depts = Department_repository.get_all()
        return [
            dept for dept in depts
            if city.lower() in dept["deptLocation"].lower()
        ]
        
    @staticmethod 
    def get_next_id(): 
        depts = Department_repository.get_all()
        return max((dept["id"] for dept in depts),default=0)+1