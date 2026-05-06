from fastapi.testclient import TestClient

from app.app import app, logger

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health_unhealthy():
    toggle = client.post("/admin/toggle-health", params={"healthy": "false"})
    assert toggle.status_code == 200

    try:
        response = client.get("/health")
        assert response.status_code == 503
        assert response.json()["detail"] == "Service Unavailable"
    finally:
        reset = client.post("/admin/toggle-health", params={"healthy": "true"})
        assert reset.status_code == 200


def test_data():
    response = client.get("/api/v1/data")
    assert response.status_code == 200
    assert "data" in response.json()


def test_logging_without_request_id_is_safe(capsys):
    logger.warning("probe without request_id")
    captured = capsys.readouterr()
    assert "Logging error" not in captured.err
