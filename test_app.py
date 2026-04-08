import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    """Test that the homepage returns 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_detects_aws_key(client):
    """Test that an AWS access key is detected"""
    response = client.post("/", data={
        "text": "AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE"
    })
    assert b"AWS Access Key" in response.data

def test_detects_password(client):
    """Test that a generic password is detected"""
    response = client.post("/", data={
        "text": "password=supersecret123"
    })
    assert b"Generic Password" in response.data

def test_clean_text_returns_no_findings(client):
    """Test that clean text returns no findings"""
    response = client.post("/", data={
        "text": "this is just a normal sentence with nothing suspicious"
    })
    assert b"No secrets detected" in response.data