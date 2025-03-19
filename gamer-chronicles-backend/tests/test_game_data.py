import pytest
from fastapi.testclient import TestClient
from io import BytesIO

@pytest.mark.parametrize("username, password, email", [
    ("testuser", "testpassword", "testuser@example.com"),
])
def test_game_data_crud(client: TestClient, username, password, email):
    # Register and Login
    client.post("/register/", json={"username": username, "password": password, "email": email})
    login_response = client.post(f"/login/?username={username}&password={password}")
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create Game Data with an image upload
    files = {"image": ("test.jpg", BytesIO(b"fake image data"), "image/jpeg")}
    game_data = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "title": "Test Game",
        "description": "This is a test game entry."
    }
    response = client.post("/game/create/", headers=headers, data=game_data, files=files)
    assert response.status_code == 200
    assert "message" in response.json()

    # Retrieve Game Data
    response = client.get("/game/")
    assert response.status_code == 200
    assert len(response.json()) > 0

    # Update Game Data
    game_id = response.json()[0]["id"]
    update_response = client.patch(f"/game/update/{game_id}", headers=headers, json={"title": "Updated Title"})
    assert update_response.status_code == 200

    # Delete Game Data
    delete_response = client.post(f"/game/delete/{game_id}", headers=headers)
    assert delete_response.status_code == 200
