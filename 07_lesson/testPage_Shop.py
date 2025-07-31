import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Page_CL_Auth import Auth
from Page_CL_CartLink import Basket
from Page_CL_User import Form
from Page_CL_Checkout import Checkout


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(45)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    page_cl_auth = Auth(driver)
    page_cl_cartlink = Basket(driver)
    page_cl_user = Form(driver)
    page_cl_checkout = Checkout(driver)
    driver.get("https://www.saucedemo.com/")
    page_cl_auth.test_standard_user()
    page_cl_cartlink.clic()
    page_cl_checkout.check()
    page_cl_user.form_name()
    page_cl_user.assert_()

    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])
    assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"


