import requests
import pytest

api_base_url = "http://0.0.0.0:8000"
token = "your-token"
model_name = "random"
user_id = "0"


def test_health_endpoint():
    """Тест эндпоинта health."""
    response = requests.get(f"{api_base_url}/health")
    assert response.status_code == 200


def test_recommendations_endpoint():
    """Тест на получение рекомендаций."""
    response = requests.get(
        f"{api_base_url}/reco/{model_name}/{user_id}",
        json={"user_id": user_id, "items": []},
    )
    assert response.status_code == 200
    recommendations = response.json().get("items", [])
    assert isinstance(recommendations, list)
    assert len(recommendations) == 10
