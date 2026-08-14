from fastapi.testclient import TestClient
from App.main import app
client=TestClient(app)

def test_login_success():
    response = client.post("/login",
                           json={
                               "username":"admin",
                               "password":"SHA1234"
                           })
    assert response.status_code == 200
    data=response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password():
    response=client.post("/login",
                         json={
                             "username":"admin",
                             "password":"wrong_password"
                         })
    
    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid username or password"

def test_login_unknown_user():
    response=client.post("/login",
                         json={
                             "username":"admin123_unknown",
                             "password":"wrong_password" 
                         })
    assert response.status_code==401
    data= response.json()
    assert data["detail"]== "Invalid username or password"
    
def test_login_missing_password():
    response=client.post("/login",
                         json={"username":"Admin"  }
                         )
    assert response.status_code==422

def test_login_missing_username():
    response=client.post("/login",
                         json={
                             "password":"SHA1234"
                         })
    assert response.status_code== 422
    data=response.json()
    # assert data["detail"]=="Unprocessable Content"
    
def test_login_empty_body():
    response=client.post("/login",
                         json={
                            
                         })
    assert response.status_code== 422
    data=response.json()
    # assert data["detail"]=="Unprocessable Content"
    
def test_login_valid_token():
    response=client.post("/login",
                         json={
                             "username":"employee",
                             "password":"SHA1234"
                         })
    assert response.status_code==200
    data=response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert len(data["access_token"])>20
    
    