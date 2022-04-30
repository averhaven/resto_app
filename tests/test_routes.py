from resto.app import create_app
import pytest

@pytest.fixture
def client_fixture():
    app = create_app(env="testing")
    client = app.test_client()
    return client

def test_not_found(client_fixture):
    response = client_fixture.get('/goat')
    assert response.status_code == 404

def test_postal_code_search(client_fixture):
    response = client_fixture.get('/recommend/restaurants?postal_code=10827')
    assert response.status_code == 200

def test_index_get(client_fixture):
    response = client_fixture.get('/')
    assert response.status_code == 200

def test_index_post(client_fixture):
    response = client_fixture.post('/',data={"postal_code":"10827"},follow_redirects=True)
    assert response.status_code == 200

def test_index_post_validate(client_fixture):
    response = client_fixture.post('/',data={"postal_code":"blabla"},follow_redirects=True)
    assert response.status_code == 200