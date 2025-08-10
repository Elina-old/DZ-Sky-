import logging
import requests
import pytest
from selenium import webdriver

base_url = "https://yougile.com/api-v2"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()

def get_token(login= 'elina.tatulyan.88@mail.ru', password = 'La_Gu_Na7'):
    key = {
        'login': login,
        'password': password,
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    resp = requests.post(base_url +'/auth/keys/get', json=key)
    token = resp.json()['key']

#Получить список ключей
def test_auth():
    key = {
        'login': 'etatulan262@xmail.ru',
        'password': 'La_Gu_Na9',
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    resp = requests.post(base_url + '/auth/keys/get', json=key)
    token = resp.json()['key']
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

# Создание нового проекта
def test_new_project():
    key = {
        'login': 'elina.tatulyan.88@mail.ru',
        'password': 'La_Gu_Na7',
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    resp = requests.post(base_url + '/auth/keys', json=key)
    token = resp.json()['key']
    headers = {
        'Proxy-Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    new_project = {
        "title": "TEST",
        "users": {"80eed1bd-eda3-4991-ac17-09d28566749d": "admin"}
    }
    resp = requests.post(base_url + '/projects', json=new_project, headers=headers)
    assert resp.status_code == 201, f'{resp.text}'


 #Создание компании (Ошибка 401)
def test_new_project_2(login= 'elina.tatulyan.88@mail.ru', password = 'La_Gu_Na7'):
    key = {
        'login': login,
        'password': password,
        'companyId': '9347006b-dc75-4550-97d5-3008ba00d4a0'
    }
    resp = requests.request( "POST",base_url + '/auth/keys', json=key)
    token = resp.json()['key']  # Здесь содержится сам токен
 # Подготовка заголовков
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
# Данные для нового проекта
    new_project = {
        "title": "TEST",
        "users": {"80eed1bd-eda3-4991-ac17-09d28566749d": "admin"}
    }
 # Отправка запроса на создание проекта
    token = resp.json()['key']
    resp = requests.request( "POST",base_url + '/projects', json=new_project, headers=headers)
    assert resp.status_code == 201, f'{resp.text}'
    print(resp.text)


#Получить список компаний
def test_company_list():
    payload = {
        "login": "elina.tatulyan.88@mail.ru",
        "password": "La_Gu_Na7",
        "name": "Elli"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", base_url +"/auth/companies", json=payload, headers=headers)
    assert response.status_code == 200
    print(response.text)
#Список ключей
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





