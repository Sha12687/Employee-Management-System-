import pytest
from fastapi.testclient import TestClient
from App.main import app
client = TestClient(app)
@pytest.fixture
def token():
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "SHA1234"
        }
    )

    assert login_response.status_code == 200
    return login_response.json()["access_token"]

@pytest.fixture
def emp_token():
    login_response = client.post(
        "/login",
        json={
            "username": "employee",
            "password": "SHA1234"
        }
    )

    assert login_response.status_code == 200
    return login_response.json()["access_token"]
    

   
def test_Check_out_without_check_in(token):
    response = client.post("/attendance/check-out",
                           headers={
                            "Authorization": f"Bearer {token}"
                           })
    assert response.status_code ==400
    assert response.json()["detail"]==("Employee is not checked in")
    
def test_employee_check_in(token):
    response = client.post(
        "/attendance/check-in",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    data = response.json()
    assert response.status_code == 201
    assert data["employee_id"] == 1
    assert data["check_out"] is None
    assert data["status"] == "Working"


def test_duplicate_check_in(token):
   
    second_response = client.post(
        "/attendance/check-in",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert second_response.status_code == 409

def test_employe_check_out(token):
    response=client.post("/attendance/check-out",
                    headers={
                    "Authorization": f"Bearer {token}"
                    })
    assert response.status_code==200
    data = response.json()
    assert data["check_out"] is not None
    assert data["status"] == "Completed"
    assert data["working_hours"] is not None
 

def  test_duplicate_check_out(token):
    response = client.post("/attendance/check-out",
                           headers={
                            "Authorization": f"Bearer {token}"
                           })
    assert response.status_code ==409
    assert response.json()["detail"]==("Employee has already checked out today")

def test_Get_my_attendance(token):
    response = client.get("/attendance/me",
                           headers={
                            "Authorization": f"Bearer {token}"
                           })
    assert response.status_code==200
    data= response.json()
    assert isinstance(data,list)

def test_admin_get_all_attendance():
    response = client.get("/attendance/me",
                           headers={
                            "Authorization": f"Bearer {token}"
                           })
    assert response.status_code==200
    data= response.json()
    assert isinstance(data,list)
    
def test_employee_denied_admin_access(emp_token):
    response = client.get("/attendance/",
                           headers={
                            "Authorization": f"Bearer {emp_token}"
                           })
    
    assert response.status_code==403
    assert response.json()["detail"] == ("Admin access required")
    
def test_filter_by_employee(token):

    response = client.get(
        "/attendance/?employee_id=1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    
def test_filter_by_employee_date(token):
    response = client.get(
        "/attendance/?date=2026-08-17",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_filter_by_employee_date_and_empId(token):
    response = client.get(
        "/attendance/?date=2026-08-17&employee_id=1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_no_matching_records(emp_token):
    response = client.get(
        "/attendance/me",
        headers={
            "Authorization": f"Bearer {emp_token}"
        }
    )
    assert response.status_code==404
    response.json()["detail"]== ("Attendance record not found for this employee")
    

