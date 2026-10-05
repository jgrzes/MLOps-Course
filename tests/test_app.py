# tests/test_main.py
from fastapi.testclient import TestClient
from main import export_envs
from settings import Settings

from app import app

client = TestClient(app)
export_envs("test")


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_settings_validation():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "fake-app-name"
