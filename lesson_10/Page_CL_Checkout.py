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


class Checkout:

    def __init__(self, driver):
        """
        Конструктор класса Checkout.
        :param driver: Webdriver- Объект драйвера Selenium
        """
        self.driver = driver


    @allure.step("Кликает соответствующую кнопку")
    def check(self):
        """
        Кнопка для проверки содержимого корзины
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']").click()
