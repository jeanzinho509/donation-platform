from tests.conftest import client

def test_create_project():
    response = client.post(
        "/projects/",
        json={"title": "Test Project", "description": "Description", "goal_amount": 1000.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Project"
    assert data["goal_amount"] == 1000.0
    assert "id" in data

def test_get_projects():
    client.post(
        "/projects/",
        json={"title": "Test Project", "description": "Description", "goal_amount": 1000.0}
    )
    response = client.get("/projects/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
