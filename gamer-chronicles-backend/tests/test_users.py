import pytest
from fastapi.testclient import TestClient

@pytest.mark.parametrize("username, password, email", [
    ("testuser", "testpassword", "testuser@example.com"),
])
def test_user_profile(client: TestClient, username, password, email):
    client.post("/register/", json={"username": username, "password": password, "email": email})

    login_response = client.post(f"/login/?username={username}&password={password}")
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/profile/", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == username

    update_response = client.patch("/user/update/", json={"email": "newemail@example.com"}, headers=headers)
    assert update_response.status_code == 200

    delete_response = client.post("/user/delete/", headers=headers)
    assert delete_response.status_code == 200
