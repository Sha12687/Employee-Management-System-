import pytest
from fastapi.testclient import TestClient
from App.main import app

client=TestClient(app)

@pytest.fixture
def admin_token():
    response = client.post("/login",
                           json={
                               "username":"admin",
                               "password":"SHA1234"
                           })
    data=response.json()
    return data["access_token"]

def test_get_employees_without_token():

    response = client.get("/employees")

    assert response.status_code == 401
    
    
def test_get_employees_invalid_token():
    response=client.get("/employees",
                        headers={
                            "Authorization":"Bearer abc123"
                        }
                        )
    assert response.status_code==401

    
def test_get_employees_valid_token(admin_token):
    response=client.get("/employees",
                        headers={
                            "Authorization":f"Bearer {admin_token}"
                        })
    assert response.status_code == 200

    assert isinstance(response.json(), list)

@pytest.fixture
def employee_token():
    response = client.post("/login",
                           json={
                                "username": "employee",
                                "password": "SHA1234"
                           })
    assert response.status_code== 200
    return response.json()["access_token"]

def test_admin_can_delete(admin_token):
    response = client.delete("/employees/6",
                          headers={
                            "Authorization":f"Bearer {admin_token}"
                          })
    assert response.status_code == 204
    

def test_admin_can_delete(admin_token):
    response =client.put("/employees/6",headers={
        "Authorization":f"Bearer {admin_token}"
    },json={
         "name": "Rahul",
         "age": 30,
         "city": "Delhi",
         "country": "Asia"
    })
    assert response.status_code==200
    
    
    