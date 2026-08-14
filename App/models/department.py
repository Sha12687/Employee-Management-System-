from pydantic import BaseModel ,Field
from typing import Optional

class CreateDepartment(BaseModel):
    deptName:str =Field(
        min_length=3,
        max_length=30,
        description="Department Name"
    )
    
    deptLocation:str =Field(
        min_length=3 ,max_length=30,
        description="Department Location"
    )

class CreateDepartmentUpdate(BaseModel):
    deptName:Optional[str] =Field(
        description="Department Name"
    )
    
    deptLocation:Optional[str] =Field(
        description="Department Location"
    )
    
class DepartmentResponse(BaseModel):
    id:int 
    deptName:str
    deptLocation:str