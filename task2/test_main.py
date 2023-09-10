# tests/test_app.py

import pytest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)


sample_item = {"name": "Kinlani"}

def test_create_person():
    response = client.post("/api/", json=sample_item)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **sample_item}

def test_read_person():
    response = client.get("/api/Kinlani")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **sample_item}

def test_update_person():
    updated_item_data = {"name": "Kinlani"}
    response = client.put("/api/Kinlani", json=updated_item_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **updated_item_data}

def test_delete_person():
    response = client.delete("/api/Kinlani")
    assert response.status_code == 200

def test_read_person_not_found():
    response = client.get("/api/Kinlani")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_update_person_not_found():
    updated_item_data = {"name": "Kinlani"}
    response = client.put("/api/Kinlani", json=updated_item_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_person_not_found():
    response = client.delete("/api/Kinlani")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
