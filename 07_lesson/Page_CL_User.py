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

class Form:

    def __init__(self, driver):
        self.driver = driver


    def form_name(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='first-name']")
        search_box.send_keys("Elina")

        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='last-name']")
        search_box.send_keys("Tatulyan")

        search_box = self.driver.find_element(By.CSS_SELECTOR, "[id='postal-code']")
        search_box.send_keys("2585")

        self.driver.find_element(By.CSS_SELECTOR, "[id='continue']").click()

    def res(self):
        res = self.driver.find_element(By.CSS_SELECTOR, "[data-test='total-label'],").text
        assert int(res) == 58.29






        #total_cost = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        #total_cost_value = float(total_cost.split("$")[1])

        #assert total_cost_value == 58.29, f"{total_cost_value}"



