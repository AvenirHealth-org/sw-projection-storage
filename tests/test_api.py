from fastapi.testclient import TestClient

from app.main import app
from tests.helpers.helpers import emulator_running


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@emulator_running
def test_write_cosmosdb():
    response = client.post("/write")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
