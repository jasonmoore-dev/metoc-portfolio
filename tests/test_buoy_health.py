from fastapi.testclient import TestClient
from services.buoylab_api.app.main import app


def test_health():
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["service"] == "buoylab_api"
