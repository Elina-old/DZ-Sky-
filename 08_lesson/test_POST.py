import pytest
import requests


base_url = "https://ru.yougile.com/api-v2/projects"
TOKEN = "BearerBhaVtL8JwLLIjIZzlMev8rDLpS-hmQJTdHboQmTyS7ZLr6yh2KyLB3QYn5-3ikmZ"

@pytest.fixture(scope="module")
def test_new_project():
    headers = {
          'Authorization': f'Bearer {TOKEN}',
           'Content-Type': 'application/json'
        }
    new_project = {"title": "TEST"}

    resp = requests.post(base_url + '/projects', json=new_project, headers=headers)
    assert resp.status_code == 201

