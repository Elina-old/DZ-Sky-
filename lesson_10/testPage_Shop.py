import allure
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
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(45)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.description("Тест проверяет корректную работу интернет магазина""её бизнес процессы")
@allure.feature("Интернет магазин")
@allure.title("Тестирование интернет магазина")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет работу интернет магазина с различными операциями
    :param driver:
    :return:
    """
with allure.step("Открытие страницы и установка задержки, для полной прогрузки всех  элементов страници"):
    page_cl_auth = Auth(driver)
    page_cl_cartlink = Basket(driver)
    page_cl_user = Form(driver)
    page_cl_checkout = Checkout(driver)
with allure.step("Ссылка на веб сайт магазина"):
    driver.get("https://www.saucedemo.com/")
with allure.step("Авторизация клиента"):
    page_cl_auth.standard_user()
with allure.step("Метод для нажатия на кнопку (корзина)"):
    page_cl_cartlink.clic()
with allure.step("Открытие страницы магазина и авторизация клиента"):
    page_cl_checkout.check()
with allure.step("Форма для заполнения, данными клиента"):
    page_cl_user.form_name()
with allure.step("Клик по кнопке, для перехода на следующую страницу"):
    page_cl_user.res()
    assert int() == 58.29
