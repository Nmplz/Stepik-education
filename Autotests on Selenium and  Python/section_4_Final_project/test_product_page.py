import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

"""
    Переход на страницу.
    Нахождение кнопки. Клик по ней.
    Решение задачи с помощью данной функции.
    Метод для проверки имени.
    Метод для проверки цены.
"""


@pytest.mark.parametrize(
    "promo_offer", [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="чинить его не собираются")) for i in range(10)]
)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"

    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket_button()
    page.add_good_to_busket()
    page.solve_quiz_and_get_code()
    page.added_good_name_check()
    page.added_good_price_check()
