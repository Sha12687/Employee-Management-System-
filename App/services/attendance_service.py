from App.dependencies.auth import get_current_user
from fastapi import Depends,HTTPException,status
from datetime import datetime,timezone,timedelta
from App.repositories.attendance_repository import AttendanceRepository
class AttendanceService:

    def check_in(payload:dict):
        # 1. Get employee ID from JWT
        employee_id=payload["employee_id"]
        time_now =datetime.now(timezone.utc)
        # 2. Get today's date
        today= time_now.date()
        # 3. Check if employee already has an open attendance
        open_attendance=AttendanceRepository.get_open_attendance(employee_id)
        if open_attendance is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
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
        # 7 get IST time
        ist_now=time_now +timedelta(hours=5,minutes=30)
        # 6. Create attendance record
        new_attendance = {
            "id": attendance_id,
            "employee_id": employee_id,
            "date": today.isoformat(),
            "check_in": ist_now("%H:%M:%S"),
            "check_out": None,
            "status": "Working",
            "working_hours": None,
            "created_at": ist_now.isoformat(),
            "updated_at": ist_now.isoformat()
        }
        # 7. Get existing attendance records
        all_attendance = AttendanceRepository.get_all()

        # 8. Add new attendance
        all_attendance.append(new_attendance)
        
        # 9. Save attendance
        AttendanceRepository.save_all(all_attendance)
        # 10. Return created attendance
        return new_attendance
    def check_out():
        pass
    def get_my_attendance():
        pass
    def get_all_attendance():
        pass
    # Admin