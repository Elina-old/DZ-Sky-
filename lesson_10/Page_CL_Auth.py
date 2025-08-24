import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    """
       Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver


class Auth:

    def __init__(self, driver):
        """
               Конструктор класса Auth.
               :param driver: Webdriver- Объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Открывает страницу магазина")
    def standard_user(self):
        with allure.step(
                "Устанавливается задержка для прогрузки всех элементов (задержка в секундах)"
                " авторизация, введение имени"):
            self.driver.get("https://www.saucedemo.com/")
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
        user_name.send_keys("visual_user")

        with allure.step(
                "Устанавливается задержка для прогрузки всех элементов (задержка в секундах)"
                "авторизация, введение пароля"):

         password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        password.send_keys("secret_sauce")

        with allure.step(" Кликает на кнопку для загрузки данных клиента"):

         self.driver.find_element(By.CSS_SELECTOR, "[name='login-button']").click()
