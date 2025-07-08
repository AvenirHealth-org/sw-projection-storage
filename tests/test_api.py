from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_write_cosmosdb():
    import certifi
    import os
    print("running tests")
    print(certifi.where())
    print("request CA bundle")
    print(os.environ.get("REQUESTS_CA_BUNDLE"))
    print("curl CA bundle")
    print(os.environ.get('CURL_CA_BUNDLE'))
    import requests
    print("Cert path used:", certifi.where())
    try:
        r = requests.get("https://localhost:8081/_explorer/index.html", verify=certifi.where())
        print("Status:", r.status_code)
    except requests.exceptions.SSLError as e:
        print("SSL ERROR:", e)
    response = client.post("/write")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
