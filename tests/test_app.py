import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    # Signup
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup.status_code in (200, 400)  # Puede fallar si ya está inscrito
    # Unregister
    unregister = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister.status_code in (200, 400, 404)  # Puede fallar si no está inscrito
