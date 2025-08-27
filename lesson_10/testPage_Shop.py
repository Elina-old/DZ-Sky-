import allure
import pytest
from selenium import webdriver

from Page_CL_Auth import Auth
from Page_CL_Cartlink import Basket
from Page_CL_User import Form
from Page_CL_Checkout import Checkout


@pytest.fixture(scope="module")
def setup_driver():  # ← Переименовали фикстуру
    _driver = webdriver.Firefox()
    _driver.implicitly_wait(45)
    _driver.maximize_window()
    yield _driver
    _driver.quit()



@allure.description("Тест проверяет корректную работу интернет магазина")
@allure.feature("Интернет магазин")
@allure.title("Тестирование интернет магазина")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(setup_driver):  # ← Используем новое имя фикстуры
    driver = setup_driver  # ← Присваиваем объект драйвера переменной

    with allure.step("Инициализация страниц"):
       page_cl_auth = Auth(driver)
       page_cl_cartlink = Basket(driver)
       page_cl_user = Form(driver)
       page_cl_checkout = Checkout(driver)

    with allure.step("Открытие страницы магазина"):
      driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизация клиента"):
       page_cl_auth.standard_user()

    with allure.step("Добавление товаров в корзину"):
       page_cl_cartlink.clic()

    with allure.step("Переход к оформлению заказа"):
       page_cl_checkout.check()

    with allure.step("Заполнение данных клиента"):
       page_cl_user.form_name()

    with allure.step("Проверка итоговой суммы"):
       page_cl_user.res()
