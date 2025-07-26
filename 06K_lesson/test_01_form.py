import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver


def test_fill_form(browser):
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    first_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "first-name")))
    first_name.send_keys("Иван")

    last_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "last-name")))
    last_name.send_keys("Петров")

    addres = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "address")))
    addres.send_keys("Ленина, 55-3")

    e_mail = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "e-mail")))
    e_mail.send_keys("test@skypro.com")

    phone = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "phone")))
    phone.send_keys("+7985899998787")

    zip_code = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "zip-code")))
    zip_code.send_keys("")

    city = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "city")))
    city.send_keys("Москва")

    country = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "country")))
    country.send_keys("Россия")

    job = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "job-position")))
    job.send_keys("QA")

    company = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "company")))
    company.send_keys("SkyPro")

    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    browser.execute_script('arguments[0].scrollIntoView();', element)
    element.click()

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_code_element = browser.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_element.get_attribute(
        "class"), "Zip code is not highlighted in red!"

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"]
    for field in fields_to_check:
        element = browser.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute(
            "class"), f"{field.replace('-', ' ').title()} is not highlighted in green!"
