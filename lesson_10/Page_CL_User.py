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

class Form:

    def __init__(self, driver):
        """
           Конструктор класса Form.
          :param driver: Webdriver- Объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Форма для заполнения данными клиента, для оформления заказа")
    def form_name(self):
        """Введение имени клиента"""
        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='first-name']")
        search_box.send_keys("Elina")
        """Введение фамилии клиента"""
        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='last-name']")
        search_box.send_keys("Tatulyan")
        """Введение индекса"""
        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='postal-code']")
        search_box.send_keys("2585")

        """Клик по кнопке"""
        self.driver.find_element(By.CSS_SELECTOR, "[id='continue']").click()

    @allure.step("Получение итоговой суммы покупок, данные со страницы сайта.")
    def res(self):
        res = self.driver.find_element(By.CSS_SELECTOR, "[data-test='total-label']").text
        assert int(res) == 58.29