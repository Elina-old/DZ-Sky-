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


class Basket:

    def __init__(self, driver):
        """
            Конструктор класса Basket.
            :param driver: Webdriver- Объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Добавление товаров в корзину")
    def clic(self):
        """ Нажимает на несколько кнопок по очереди, добавляя товар в корзину.
        :param : Lisl[srt]-список текстов на кнопках которые нужно нажать.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()

