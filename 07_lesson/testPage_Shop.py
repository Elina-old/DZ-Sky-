import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Page_CL_Auth import Auth
from Page_CL_Cartlink import Basket
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
    page_cl_auth.standard_user()
    page_cl_cartlink.clic()
    page_cl_checkout.check()
    page_cl_user.form_name()
    page_cl_user.res()
    assert int() == 58.29



