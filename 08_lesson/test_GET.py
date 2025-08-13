import os
import socket
import pytest
import requests


base_url = "https://ru.yougile.com/api-v2/"

# Учётные данные (при желании переопределите через переменные окружения)
LOGIN = os.getenv("YOUGILE_LOGIN", "etatulan262@xmail.ru")
PASSWORD = os.getenv("YOUGILE_PASSWORD", "La_Gu_Na9")


@pytest.fixture(scope="session")
def require_online():
    """Скипает тесты, если хост API недоступен (например, нет DNS/интернета)."""
    try:
       socket.gethostbyname("ru.yougile.com")
    except Exception as exc:
       pytest.skip(f"API host not resolvable: {exc}")


def _request_companies(login: str, password: str):
    """Запрашивает список компаний для указанных логина/пароля (постраничный ответ)."""
    body = {
       "login": login,
       "password": password,
       "name": "",
    }
    headers = {"Content-Type": "application/json"}
    resp = requests.post(base_url + "auth/companies", json=body, headers=headers)
    assert resp.status_code == 200, f"auth/companies failed: {resp.text}"
    return resp.json()


def _request_token(login: str, password: str, company_id: str) -> str:
    """Создаёт/получает ключ API через endpoint auth/keys и возвращает строку ключа."""
    body = {
       "login": login,
       "password": password,
       "companyId": company_id,
    }
    headers = {"Content-Type": "application/json"}
    resp = requests.post(base_url + "auth/keys", json=body, headers=headers)
    assert resp.status_code in (200, 201), f"auth/keys failed: {resp.status_code} {resp.text}"
    data = resp.json()
    token = data.get("key") or data.get("token")
    assert token, f"Token not found in response: {data}"
    return token


@pytest.fixture()
def fresh_token() -> str:
    """Фикстура: получает токен перед тестом и возвращает его без префикса 'Bearer'."""
    companies = _request_companies(LOGIN, PASSWORD)
    assert isinstance(companies, dict) and "content" in companies, "Unexpected companies response format"
    company_list = companies.get("content", [])
    assert isinstance(company_list, list) and len(company_list) > 0, "No companies available for provided credentials"
    company_id = company_list[0]["id"]
    return _request_token(LOGIN, PASSWORD, company_id)

#Позитивная проверка(Получить детали)
def test_get_companies(fresh_token):
    headers = {
        "Authorization": f"Bearer {fresh_token}",
         "Content-Type": "application/json"
    }
    response = requests.get(base_url + 'companies', headers=headers)
    assert response.status_code == 200

#Негативная проверка, получить детали( с не валидным  headers)
def test_get_companies_negative(fresh_token):
    headers = {
        "Authorization": f"Bearer ",
         "Content-Type": "application/json"
    }
    response = requests.get(base_url + 'companies', headers=headers)
    assert response.status_code == 401
