import requests
import pytest
import json


base_url = "https://ru.yougile.com/api-v2/{resource}"
TOKEN = "Bearer QgfiL35vqpmXgGX0JB-Wdl4nr6c3V2ujGvk26fI-GWukUKdtdBPUVHcSIGTNWq3C"

def test_get_project_list():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
         "Content-Type": "application/json"
    }
    response = requests.get(base_url + 'projects', headers=headers)
    assert response.status_code == 201, f'{response.text}'

#негативная проверка (запрос без токина)
def test_get_project_list_negative():
    headers = {
        "Authorization": f"Bearer",
        "Content-Type": "application/json"
    }
    response = requests.get(base_url + 'projects', headers=headers)
    assert response.status_code == 201, f'{response.text}'




