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


class Basket:

    def __init__(self, driver):
        self.driver = driver



    def string(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

        self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

        self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']").click()


    def cart_link(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()




