import requests
import pytest
from selenium import webdriver
import requests
import pytest
from selenium.webdriver.firefox import webdriver

base_url = "https://yougile.com/api-v2"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver

#Получить список ключей (работает)
def test_auth():
    key = {
        'login': 'etatulan262@xmail.ru',
        'password': 'La_Gu_Na9',
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    resp = requests.post(base_url + '/auth/keys/get', json=key)
    token = resp.json()
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    print(resp.text)


# Создание нового проекта(ошибка 401)
def test_new_project():
    key = {
        'login': 'elina.tatulyan.88@mail.ru',
        'password': 'La_Gu_Na7',
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    new_project = {
        'title': 'TEST',
        'users': {'80eed1bd-eda3-4991-ac17-09d28566749d': 'admin'}
    }
    resp = requests.post(base_url + '/auth/keys/get', json=key)
    token = resp.json()

    my_header = {'key'}
    resp = requests.post(base_url + '/projects', json=new_project)
    assert resp.status_code == 200
    print(resp.text)

# Получить список компаний код=200
def test_paylo_ad():
    payload = {
        'login': 'etatulan262@xmail.ru',
        'password': 'La_Gu_Na9',
        'name': 'Элина'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", base_url+"/auth/companies", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print(response.text)



