from fastapi import APIRouter, Depends
from App.services.attendance_service import AttendanceService
from App.dependencies.auth import get_current_user, require_admin
from datetime import date

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/check-in")
def check_in(
    payload: dict = Depends(get_current_user)
):
    return AttendanceService.check_in(payload)


@router.post("/check-out")
def check_out(
    payload: dict = Depends(get_current_user)
):
    return AttendanceService.check_out(payload)


@router.get("/me")
def get_my_attendance(
    payload: dict = Depends(get_current_user)
):
    return AttendanceService.get_emp_attendance(payload)


@router.get("/")
def get_all_attendance(
    employee_id: int | None = None,
    date: date | None = None,
    payload: dict = Depends(require_admin)
):

    # Employee + Date
    if employee_id is not None and date is not None:
        return AttendanceService.get_all_attendance_By_date_and_empid(
            payload,
            date,
            employee_id
        )

    # Employee only
    if employee_id is not None:
        return AttendanceService.get_all_attendance(
            payload,
            employee_id
        )

    # Date only
    if date is not None:
        return AttendanceService.get_all_attendance_By_date(
            payload,
            date
        )

    # All attendance
    return AttendanceService.get_all_attendance(
        payload,
        None
    )


@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    payload: dict = Depends(require_admin)
):
    return AttendanceService.delete_attendance(attendance_id)