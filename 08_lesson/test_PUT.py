import pytest
import requests

base_url = "https://ru.yougile.com/api-v2/"
TOKEN = "Bearer BhaVtL8JwLLIjIZzlMev8rDLpS-hmQJTdHboQmTyS7ZLr6yh2KyLB3QYn5-3ikmZ"

@pytest.fixture(scope="module")
def test_update(response=None):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    new_project = {"title": "Test_3"}
    my_id = response.json()["id": "84dfafe0-f409-43f6-8f0b-8511f6056427"]

    response = requests.put(base_url + 'projects/' + my_id, json=new_project, headers=headers)
    assert response.status_code == 200


