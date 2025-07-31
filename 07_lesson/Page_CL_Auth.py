import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver



class Auth:

    def __init__(self, driver):
        self.driver = driver


    def test_standard_user(self):
        self.driver.get("https://www.saucedemo.com/")
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
        user_name.send_keys("visual_user")

        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        password.send_keys("secret_sauce")

        self.driver.find_element(By.CSS_SELECTOR, "[name='login-button']").click()


#Создать класс для страницы авторизации, который будет содержать методы для ввода логина и пароля, а также для нажатия кнопки входа.
