import pytest
from fastapi.testclient import TestClient

@pytest.mark.parametrize("username, password, email", [
    ("testuser", "testpassword", "testuser@example.com"),
])
def test_register_and_login(client: TestClient, username, password, email):
    # Register User
    response = client.post("/register/", json={"username": username, "password": password, "email": email})
    assert response.status_code == 200

    # Login User
    response = client.post(f"/login/?username={username}&password={password}")
    assert response.status_code == 200
    assert "token" in response.json()
