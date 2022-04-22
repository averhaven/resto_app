from resto import create_app
import pytest

@pytest.fixture
def client_fixture():
    app = create_app()
    client = app.test_client()
    return client

def test_not_found(client_fixture):
    response = client_fixture.get('/goat')
    assert response.status_code == 404