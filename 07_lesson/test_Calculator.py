import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from Page_CL_calc import CalcPage

@pytest.fixture(scope="module")
def driver():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(45)
        driver.maximize_window()
        yield driver

def test_calculator(driver):
    page_cl_calc = CalcPage(driver)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page_cl_calc.search_box()
    page_cl_calc.open_calculator()



