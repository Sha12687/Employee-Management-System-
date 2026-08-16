from pydantic import BaseModel
from typing import Optional


class Attendance(BaseModel):
    id: int
    employee_id: int
    date: str
    check_in: str
    check_out: Optional[str] = None
    status: str
    working_hours: Optional[float] = None
    
class AttendanceResponse(BaseModel):
    message: str
    attendance: Attendance

class UpdateAttendance(BaseModel):
    check_in: str | None = None
    check_out: str | None = None
    status: str | None = None