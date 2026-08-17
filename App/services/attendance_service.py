from App.dependencies.auth import get_current_user
from fastapi import Depends,HTTPException,status
from datetime import datetime,timezone,timedelta
from zoneinfo import ZoneInfo
from datetime import date
from App.repositories.attendance_repository import AttendanceRepository
class AttendanceService:

    def check_in(payload:dict):
        # 1. Get employee ID from JWT
        employee_id=payload["employee_id"]
        time_now =datetime.now(ZoneInfo("Asia/Kolkata"))
        # 2. Get today's date
        today= time_now.date()
        # 3. Check if employee already has an open attendance
        open_attendance=AttendanceRepository.get_open_attendance(employee_id)
        if open_attendance is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Employee is already checked in"
            )
        # 4. Check if attendance already exists for today
        already_checked_in= AttendanceRepository.get_by_employee_and_date(employee_id,today)
        if already_checked_in is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Attendance already exists for today"
            )
        attendance_id=AttendanceRepository.get_next_id()
        # 6. Create attendance record
        new_attendance = {
            "id": attendance_id,
            "employee_id": employee_id,
            "date": today.isoformat(),
            "check_in": time_now.strftime("%H:%M:%S"),
            "check_out": None,
            "status": "Working",
            "working_hours": None,
            "created_at": time_now.isoformat(),
            "updated_at": time_now.isoformat()
        }
        # 7. Get existing attendance records
        all_attendance = AttendanceRepository.get_all()

        # 8. Add new attendance
        all_attendance.append(new_attendance)
        
        # 9. Save attendance
        AttendanceRepository.save_all(all_attendance)
        # 10. Return created attendance
        return new_attendance
    def check_out(payload:dict):
        # 1. Get employee ID from JWT
        employee_id=payload["employee_id"]
        ist_now = datetime.now(ZoneInfo("Asia/Kolkata"))
        # 2. Get today's date
        today= ist_now.date()
        # . check if employee already check-out for today
        is_emp_already_chekout_today=AttendanceRepository.get_close_attendance(employee_id,today)
        if is_emp_already_chekout_today is not None :
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Employee has already checked out today"
            )
        # 3. Check if employee already has an open attendance
        open_attendance=AttendanceRepository.get_open_attendance(employee_id)
        if open_attendance is  None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee is not checked in"
            )
        check_in_time = datetime.strptime(
        open_attendance["check_in"],
        "%H:%M:%S" 
        )
        # Keep the time 09:02:15, but attach today's date and India's timezone to it
        check_in_time = check_in_time.replace(
        year=ist_now.year,
        month=ist_now.month,
        day=ist_now.day,
        tzinfo=ZoneInfo("Asia/Kolkata")
             )
        working_hours=ist_now-check_in_time
        # Convert the working time to hours and keep 2 decimal places.
        working_hours = round(
        working_hours.total_seconds() / 3600,
        2
        )
        fetch_attendance=AttendanceRepository.get_by_id(open_attendance["id"])
        if fetch_attendance is None:
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Attendance record not found"
            )
        fetch_attendance["check_out"]=ist_now.strftime("%H:%M:%S")
        fetch_attendance["status"]="Completed"
        fetch_attendance["working_hours"]=working_hours
        fetch_attendance["updated_at"] = ist_now.isoformat()
        AttendanceRepository.update_attendance(fetch_attendance)
        return fetch_attendance
    def get_emp_attendance(payload:dict ):
        employee_id=payload["employee_id"]
        my_attendance=AttendanceRepository.get_by_employee_id(employee_id)
        if not my_attendance :
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found for this employee"
            )
        return my_attendance
        
    def get_all_attendance(payload:dict,employee_id: int | None = None):
        all_attendance=AttendanceRepository.get_all()
        if employee_id is not None:
            return [
            attendance
            for attendance in all_attendance
            if attendance["employee_id"] == employee_id
                ]
        return all_attendance
    
    def get_all_attendance_By_date(payload:dict,date:date |None =None):
        if date is not None:
            all_attendance_by_date=AttendanceRepository.get_all_employee_attendance_by_date(date)
            if not all_attendance_by_date:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No record found at this date"
                )
            return all_attendance_by_date
    
    def get_all_attendance_By_date_and_empid(payload:dict,
                                             date:date |None =None,
                                             employee_id:int |None =None):
        
        all_attendance_by_date=AttendanceRepository.get_all_employee_attendance_by_date_empid(date,employee_id)
        if not all_attendance_by_date:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No record found"
                )
        return all_attendance_by_date
        
    @staticmethod
    def delete_attendance(attendance_id: int):
        attendance = AttendanceRepository.get_by_id(attendance_id)
        if attendance is None:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found"
        )
        deleted_attendance = AttendanceRepository.delete_attendance(
        attendance_id) 
        return deleted_attendance

    
