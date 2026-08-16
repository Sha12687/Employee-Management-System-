
import pytest
from fastapi.testclient import TestClient
from App.main import app

client = TestClient(app)



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


def test_admin_can_delete(admin_token):
    response = client.delete("/employees/6",
                          headers={
                            "Authorization":f"Bearer {admin_token}"
                          })
    assert response.status_code == 204
    

def test_admin_can_update_employee(admin_token):
    response =client.put("/employees/7",headers={
        "Authorization":f"Bearer {admin_token}"
    },json={
         "name": "Rahul",
         "age": 30,
         "city": "Delhi",
         "country": "Asia"
    })
    assert response.status_code==200
    
    
    
    