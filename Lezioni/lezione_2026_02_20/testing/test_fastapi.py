import pytest
from fastapi.testclient import TestClient
from main import app

# 1. Facciamo la/e fixture di setup
def client():
    with TestClient(app) as test_client:
        yield test_client

    # Posto dove metteremo "Teardown" <- Chiusura di file, sessioni, connessioni etc

# Funzione di test dell'api
def test_read_main(client):
    response = client.get("/")  # Otteniamo il percorso di root dell'api
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world'}