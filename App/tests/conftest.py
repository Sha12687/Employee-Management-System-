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

@pytest.fixture
def employee_token():
    response = client.post("/login",
                           json={
                                "username": "employee",
                                "password": "SHA1234"
                           })
    assert response.status_code== 200
    return response.json()["access_token"]