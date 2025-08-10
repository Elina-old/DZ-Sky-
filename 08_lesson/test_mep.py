import requests
import pytest
import json
from selenium import webdriver

base_url = "https://yougile.com/api-v2"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()

#ГЕТ ЗАПРОС
def test_get_token(login= 'elina.tatulyan.88@mail.ru', password = 'La_Gu_Na7'):
    key = {
        'login': login,
        'password': password,
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    headers = {"Content-Type": "application/json"}
    resp = requests.request( "POST",base_url +'/auth/keys/get',headers=headers, json=key)
    assert resp.status_code == 200
    print(resp.text)

#Приглосить в компанию
def test_users():
    payload = {
        "email": "etatulan262@gmail.com",
        "isAdmin": False
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer VBEDkDjX6uTl3crdZS+tWXIb0JhykWR9w4BarsEHYkQ3jgH9g+WG0vRPo2fT61n2"
    }
    response = requests.request("POST",base_url, json=payload, headers=headers)
    assert response.status_code == 200
    print(response.text)

def test_get_list():
    querystring = {"limit": "50", "offset": "0", "email": "elina.tatulyan.88@mail.ru",
                   "projectId": "84dfafe0-f409-43f6-8f0b-8511f6056427"}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer VBEDkDjX6uTl3crdZS+tWXIb0JhykWR9w4BarsEHYkQ3jgH9g+WG0vRPo2fT61n2"
    }
    response = requests.request("GET", base_url, headers=headers)
    assert response.status_code == 200
    print(response.text)

def test_get_3():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer VBEDkDjX6uTl3crdZS+tWXIb0JhykWR9w4BarsEHYkQ3jgH9g+WG0vRPo2fT61n2"
    }
    response = requests.request("GET", base_url + "/users", headers=headers)
    assert response.status_code == 200
    print(response.text)

#Изменить
def test_put():
    payload = {"isAdmin": False}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer FJvzqi+ui7gZoxWtW7RZjJv-eB9AciALESKwHKBe63SEZospWDL6hDAZusuedw3k"
    }
    response = requests.request("PUT",base_url, json=payload, headers=headers)
    assert response.status_code == 200
    print(response.text)

# Создание нового проекта
def test_new_project():
    new_project = {
        "title": "TEST",
        "users": {"80eed1bd-eda3-4991-ac17-09d28566749d": "admin"}
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer FJvzqi+ui7gZoxWtW7RZjJv-eB9AciALESKwHKBe63SEZospWDL6hDAZusuedw3k"
    }
    resp = requests.post(base_url + '/projects', json=new_project, headers=headers)
    assert resp.status_code == 201
    assert resp.status_code == 201, f'{resp.text}'
    print(resp.text)


