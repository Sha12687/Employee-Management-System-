from App.utils.json_service import JsonService
from App.config.setting import Settings

class AttendanceRepository:

    @staticmethod
    def get_all():
        return JsonService.read_file(Settings.ATTENDANCE_FILE)

    @staticmethod
    def save_all(attendance):
        JsonService.write_file(Settings.ATTENDANCE_FILE,attendance)

    @staticmethod
    def get_next_id():
        Data= AttendanceRepository.get_all()
        return max((attendance["id"] for attendance in Data),default=0)+1
    
    @staticmethod
    def get_by_employee_and_date(employee_id, date):
        attendance_records= AttendanceRepository.get_all()
        for record in attendance_records:
            if (
                record["employee_id"] == employee_id
                and record["date"] == date.isoformat()
            ):
                return record
        
        return None


    @staticmethod
    def get_open_attendance(employee_id):
        attendance_records= AttendanceRepository.get_all()
        for record in attendance_records:
            if (
                record["employee_id"]==employee_id and 
                record["check_out"] is None
            ):
                return record
        return None
    
    @staticmethod
    def get_by_id(att_id:int):
        all_attendence=AttendanceRepository.get_all()
        for record in all_attendence:
            if(
                record["id"]==att_id 
            ):
                return record
        
        return None
    @staticmethod
    def delete_attendance(id:int):
        attendence = AttendanceRepository.get_by_id(id)
        if attendence is None:
            return None
        all_attendence=AttendanceRepository.get_all()
        all_attendence.remove(attendence)
        AttendanceRepository.save_all(all_attendence)
        return attendence
    
    
    @staticmethod
    def update_attendance(attendance):
        if attendance is None:
            return None
        all_attendance=AttendanceRepository.get_all()
        for existing_attendance in all_attendance:
            if existing_attendance["id"] == attendance["id"]:
                existing_attendance.update(attendance)
                AttendanceRepository.save_all(all_attendance)
                return attendance
        return None
    
    
        
        