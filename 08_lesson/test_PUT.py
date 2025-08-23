import os
import socket
import pytest
import requests


base_url = "https://ru.yougile.com/api-v2/"
LOGIN = os.getenv("YOUGILE_LOGIN", "elina.tatulyan.88@mail.ru")
PASSWORD = os.getenv("YOUGILE_PASSWORD", "Na_Gu_La7")


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

def test_company_list(require_online):
    companies = _request_companies(LOGIN, PASSWORD)
    assert isinstance(companies, dict) and "content" in companies, "Companies response is not a paged object"
    assert isinstance(companies["content"], list) and len(companies["content"]) >= 1, "Expected at least one company"

 #Позитивная проверка
def test_edit_project(require_online, fresh_token: str):
    new_project = {"title": "TEST"}
    headers = {
       "Authorization": "Bearer {fresh_token}",
       "Content-Type": "application/json",
    }
    resp = requests.post(base_url + "projects", json=new_project, headers=headers)
    assert resp.status_code == 201, "Create project failed: {resp.status_code} {resp.text}"
    response_data = resp.json()
    project_id = response_data["id"]
    assert project_id, "Project id is empty"

    new_project = {"title": "TEST_2"}
    headers = {
        "Authorization": f"Bearer {fresh_token}",
        "Content-Type": "application/json",
    }
    resp = requests.put(base_url + "projects/" + "project_id", json=new_project, headers=headers)
    assert resp.status_code == 200, "Create project failed: {resp.status_code} {resp.text}"
    assert resp.json()["description"] == new_project


 #Негативная проверка (запрос без id)
def test_edit_project_negative(require_online, fresh_token: str):
    new_project = {"title": "TEST"}
    headers = {
        "Authorization": f"Bearer {fresh_token}",
        "Content-Type": "application/json",
    }
    resp = requests.post(base_url + "projects", json=new_project, headers=headers)
    assert resp.status_code == 201, f"Create project failed: {resp.status_code} {resp.text}"
    response_data = resp.json()
    project_id = response_data["id"]
    assert project_id, "Project id is empty"

    new_project = {"title": "TEST_2"}
    headers = {
        "Authorization": f"Bearer {fresh_token}",
        "Content-Type": "application/json",
    }
    resp = requests.put(base_url + "projects/" , json=new_project, headers=headers)
    assert resp.status_code == 404, f"Create project failed: {resp.status_code} {resp.text}"


