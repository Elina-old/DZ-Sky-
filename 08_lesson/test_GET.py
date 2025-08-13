import requests
import pytest

base_url = "https://ru.yougile.com/api-v2/"
TOKEN = "BearerQgfiL35vqpmXgGX0JB-Wdl4nr6c3V2ujGvk26fI-GWukUKdtdBPUVHcSIGTNWq3C"

@pytest.fixture
def test_get_project_list():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
         "Content-Type": "application/json"
    }
    response = requests.get(base_url + 'projects', headers=headers)
    assert response.status_code == 200
    assert response.status_code == 201, f'{response.text}'