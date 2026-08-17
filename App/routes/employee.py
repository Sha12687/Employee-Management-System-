from fastapi import APIRouter ,status,HTTPException,Query,Depends
from App.services.employee_service import EmployeeService
from App.dependencies.auth import get_current_user ,require_admin
from App.models.employee import (
    EmployeeResponse,
    CreateEmployeeUpdate,
    CreateEmployee)
router =APIRouter(
    prefix="/employees",
    tags=["Employees"]
    )
@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get all employees",
    description="Returns all employees or filters employees by city."
    )
def get_employees(name: str | None = Query(
    default=None,
    description="Filter employees by name"),
    current_user :dict =Depends(get_current_user)):
    if name:
        employees=EmployeeService.search_employee(name)
    else:  
        employees = EmployeeService.get_all_employees()
    return [EmployeeResponse(**employee) for employee in employees]
    
@router.delete(
        "/{id}",
        status_code =status.HTTP_204_NO_CONTENT,
        summary="Delete employee"
    )
def delete_employee(id:int,
                    current_user: dict = Depends(require_admin)):
    deleted_employee = EmployeeService.delete_employee(id)
    if not deleted_employee:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee {id} not found"
        )
    return 

@router.post(
    "",
    response_model=EmployeeResponse,
    summary="Create employee",
    status_code=status.HTTP_201_CREATED
    )
def create_employee(employee: CreateEmployee):
    create_emp= EmployeeService.add_employee(employee)
    return EmployeeResponse(**create_emp)

@router.put(
    "/{id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Update employee"
    )
def update_employee(id:int , employee:CreateEmployeeUpdate,
                    user:dict = Depends(require_admin)):
    update_emp=EmployeeService.update_employee(id,employee)
    if update_emp is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee {id} not found"
        )
    return EmployeeResponse(**update_emp)
