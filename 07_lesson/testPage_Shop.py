import pytest
from selenium import webdriver

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


    driver.quit()
