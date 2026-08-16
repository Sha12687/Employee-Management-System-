from fastapi import APIRouter,status,HTTPException,Query
from App.models.department import DepartmentResponse,CreateDepartment,CreateDepartmentUpdate
from App.services.department_service import Department_repository
router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[DepartmentResponse],
    )
def get_department(city:str |None = Query(
    default=None,
    description="Filter Department by location")):
    if city:
        data=DepartmentService.get_department_by_city(city)
    else:
        data=DepartmentService.get_all_department();
    return [DepartmentResponse(**dept) for dept  in data ]

@router.post(
    "",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Department"
)
def create_department(dept:CreateDepartment):
    deptCreated=DepartmentService.add_department(dept)
    return DepartmentResponse(**deptCreated)

@router.put(
    "/{id}",
    response_model=CreateDepartmentUpdate,
    status_code=status.HTTP_202_ACCEPTED,
    description="Department Update"
)
def update_Department(id :int , dept:CreateDepartmentUpdate):
    dept = DepartmentService.update_department(id,dept)
    if dept is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department {id} not found"
        )
    return DepartmentResponse(**dept)
@router.delete(
    "/{id}",
    response_model=DepartmentResponse,
    description="Delete Department"  ,
    status_code=status.HTTP_200_OK 
    )
def delete_department(id:int):
    data=DepartmentService.delete_department(id)
    if not data:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Department {id} not found"
        )
    return DepartmentResponse(**data)

