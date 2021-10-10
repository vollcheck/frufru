import falcon
from falcon import testing
import pytest

from frufru.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_get_car(client):
    doc = {"make": "Volkswagen", "model": "Golf"}
    response = client.simulate_get("/cars")
    assert response.json == doc
    assert response.status == falcon.HTTP_OK
