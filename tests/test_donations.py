from tests.conftest import client

def test_register_and_login():
    response = client.post(
        "/register",
        json={"name": "Test User", "email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 201

    response = client.post(
        "/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_donation():
    # 1. Register and login
    client.post(
        "/register",
        json={"name": "Test User", "email": "test@example.com", "password": "password123"}
    )
    login_response = client.post(
        "/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create project
    project_response = client.post(
        "/projects/",
        json={"title": "Test Project", "description": "Description", "goal_amount": 1000.0}
    )
    project_id = project_response.json()["id"]

    # 3. Create donation
    response = client.post(
        "/donations/",
        json={"project_id": project_id, "amount": 100.0},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 100.0
    assert data["project_id"] == project_id
    assert "receipt_id" in data
    assert "receipt_hash" in data
