from fastapi.testclient import TestClient
from cint.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'mapping': True, 'sandbox_ok': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'mapping': True}).json()
    assert bad["passed"] is False
    assert "sandbox" in bad["failed"]
