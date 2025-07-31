import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver



@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

class CalcPage:

    def __init__(self, driver):
        self.driver = driver



    def open_calculator(self):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
            delay_input.clear()
            delay_input.send_keys("45")

    def search_box(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay.clear()
        delay.send_keys("45")

        self.driver .find_element(By.XPATH, '//span[text()="7"]').click()

        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()

        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()

        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
        )








