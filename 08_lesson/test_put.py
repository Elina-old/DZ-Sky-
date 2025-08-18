import pytest
import requests

base_url = "https://ru.yougile.com/api-v2/{resource}"
TOKEN = "Bearer BhaVtL8JwLLIjIZzlMev8rDLpS-hmQJTdHboQmTyS7ZLr6yh2KyLB3QYn5-3ikmZ"

def test_update():
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    project = {"title": "Test_3"}

    resp = requests.post(base_url + 'projects', json=project, headers=headers)
    assert resp.status_code == 201, f'{resp.text}'
    response_data = resp.json()
    project_id = response_data["id"]
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    new_project = {"title": "Test_4"}
    resp = requests.put(base_url + '/projects', json=new_project, headers=headers)
    assert resp.status_code == "", f'{resp.text}'
    print(resp.text)

