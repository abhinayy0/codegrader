from project.tests.base import client
from project import db
from project.api.models import User
import json

def test_users(client):
    """Start with a blank database."""

    rv = client.get('/users/ping')
    
    assert rv.json == {"status": "success", 'message':"pong"}
    
def test_add_user(client):
    rv = client.post("/users", json={"username":"abhinay", "email":"abhinay@gmail.com"})
    assert rv.status_code == 201
    assert rv.json == {"status":"success", "message": "abhinay@gmail.com was added!"}

def test_add_invalid_user_json(client):
    rv = client.post("/users", json={})
    assert rv.status_code == 400
    assert rv.json == {"status":"fail", "message": "Invalid payload"}

def test_add_invalid_user_json_keys(client):
    rv = client.post("/users", json={"email":"abhinay@gmail.com"})
    assert rv.status_code == 400
    assert rv.json == {"status":"fail", "message": "Invalid payload"}

def test_add_user_duplicate_email(client):
    client.post("/users", json={"username":"abhinay","email":"abhinay@gmail.com"})
    rv = client.post("/users", json={"username":"abhinay","email":"abhinay@gmail.com"})
    assert rv.status_code == 400
    assert rv.json == {"status":"fail", "message": "Sorry that email already exists."}

def test_single_user(client):
    user = User(username="abhinay",email="abhinay@gmail.com")
    db.session.add(user)
    db.session.commit()
    rv = client.get(f"/users/{user.id}")
    assert rv.json == {"username":"abhinay", "email":"abhinay@gmail.com"}
    assert rv.status_code == 200