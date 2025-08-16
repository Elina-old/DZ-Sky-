import pytest
import requests
import json

base_url = "https://ru.yougile.com/api-v2/"
TOKEN = "Bearer BhaVtL8JwLLIjIZzlMev8rDLpS-hmQJTdHboQmTyS7ZLr6yh2KyLB3QYn5-3ikmZ"

def test_company_list():
    body = {
         "login": "elina.tatulyan.88@mail.ru",
          "password": "La_Gu_Na7",
          "name": ""
    }
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(base_url + 'auth/companies', json=body, headers=headers)
    assert resp.status_code == 200 , f'{resp.text}'
    print(resp.text)

def test_new_project():
    new_project = {"title": "TEST"}
    headers = {
          'Authorization': f'Bearer {TOKEN}',
           'Content-Type': 'application/json'
        }
    resp = requests.post(base_url + 'projects', json=new_project, headers=headers)
    assert resp.status_code == 201, f'{resp.text}'
    response_data = resp.json()
    project_id = response_data["id"]
    return project_id

#негативная проверка, создание проекта без названия
def test_new_project_negativ():
    headers = {
          'Authorization': f'Bearer {TOKEN}',
           'Content-Type': 'application/json'
        }
    new_project = {"title": ""}

    resp = requests.post(base_url + 'projects', json=new_project, headers=headers)
    assert resp.status_code == 200, f'{resp.text}'
