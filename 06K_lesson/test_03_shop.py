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

def test_standard_user(browser):
    browser.get("https://www.saucedemo.com/")

    user_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
    user_name.send_keys("visual_user")


#авторизация
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
    password.send_keys("secret_sauce")


    browser.find_element(By.CSS_SELECTOR, "[name='login-button']").click()


#добавление в карзину
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    browser.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    browser.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']").click()

#переход в карзину
    browser.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()

#нажать Checkout
    browser.find_element(By.CSS_SELECTOR, "[id='checkout']").click()

#заполнение формы


    search_box = browser.find_element(By.CSS_SELECTOR, "[id='first-name']")
    search_box.send_keys("Elina")

    search_box = browser.find_element(By.CSS_SELECTOR, "[id='last-name']")
    search_box.send_keys("Tatulyan")

    search_box = browser.find_element(By.CSS_SELECTOR, "[id='postal-code']")
    search_box.send_keys("2585")

    browser.find_element(By.CSS_SELECTOR, "[id='continue']").click()

    total_cost = browser.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    # Проверка итоговой суммы
    assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"


    browser.quit()



