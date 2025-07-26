import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver


def test_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    delay = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay.clear()
    delay.send_keys("45")


    browser.find_element(By.XPATH, '//span[text()="7"]').click()

    browser.find_element(By.XPATH, '//span[text()="+"]').click()

    browser.find_element(By.XPATH, '//span[text()="8"]').click()

    browser.find_element(By.XPATH, '//span[text()="="]').click()

    WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
    )


    result = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15

    browser.quit()


