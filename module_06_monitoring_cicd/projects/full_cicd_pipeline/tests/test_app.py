from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ML Pipeline Active"}

def test_predict():
    payload = {"feature1": 10.0, "feature2": 5.0}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    # 10*0.5 + 5*0.2 = 5.0 + 1.0 = 6.0
    assert response.json()["prediction"] == 6.0

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
