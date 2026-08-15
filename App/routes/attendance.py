from fastapi import FastAPI,Depends,APIRouter
from App.services.attendance_service import AttendanceService
from App.dependencies.auth import get_current_user

router =APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post("/check-in")
def check_in(payload:dict = Depends(get_current_user)):
    return AttendanceService.check_in(payload)