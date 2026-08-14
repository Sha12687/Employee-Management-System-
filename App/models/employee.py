from pydantic import BaseModel, Field
from typing import Optional
class CreateEmployee(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=30,
        description="Employee name"
    )

    age: int = Field(
        ge=10,
        le=60,
        description="Employee age"
    )

    city: str = Field(
        min_length=3,
        max_length=30,
        description="Employee city"
    )

    country: str = Field(
        default="India",
        description="Employee country"
    )

class EmployeeResponse(BaseModel):
        id: int
        name: str
        age: int
        city: str
        country: str
    
class CreateEmployeeUpdate(BaseModel):
        name: Optional[str]=Field(
        default=None,
        min_length=3,
        max_length=30,
        description="Employee name",
    )
        age :Optional[int] = Field(
        default=None,
        ge=10,le=60,
        description="Employee age"
    )
        city :Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=30,
        description="Employee City"
    )
        country : Optional[str] = None
    
    
