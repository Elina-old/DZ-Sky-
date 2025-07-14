

from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # или Firefox()
    yield driver
    driver.quit()

    def test_example(driver):
        driver.get("http://example.com")
        assert "Example Domain" in driver.title

def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

with pytest.raises(NoSuchElementException):
     driver.find_element(By.ID, 'box0')


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

search_box = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
search_box.send_keys("tomsmith")
sleep(5)

search_box = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
search_box.send_keys("SuperSecretPassword!")
sleep(5)

search_box = driver.find_element(By.CSS_SELECTOR, "button.radius")
search_box.send_keys("Login")
search_box.click()
sleep(5)
