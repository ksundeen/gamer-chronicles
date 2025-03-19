import pytest
from fastapi.testclient import TestClient

@pytest.mark.parametrize("username, password, email", [
    ("testuser", "testpassword", "testuser@example.com"),
])
def test_user_profile(client: TestClient, username, password, email):
    # Register User
    client.post("/register/", json={"username": username, "password": password, "email": email})

    # Login and get token
    login_response = client.post(f"/login/?username={username}&password={password}")
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get User Profile
    response = client.get("/user/profile/", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == username

    # Update User Profile
    update_response = client.patch("/user/update/", json={"email": "newemail@example.com"}, headers=headers)
    assert update_response.status_code == 200

    # Delete User
    delete_response = client.post("/user/delete/", headers=headers)
    assert delete_response.status_code == 200
