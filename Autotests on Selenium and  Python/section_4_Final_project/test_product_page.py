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


# @pytest.mark.parametrize(
#     "promo_offer",
#     [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="чинить не собираются")) for i in range(10)],
# )
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"

#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_busket_button()
#     page.add_good_to_busket()
#     page.solve_quiz_and_get_code()
#     page.added_good_name_check()
#     page.added_good_price_check()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.add_good_to_busket()
#     page.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.should_not_be_success_message()


# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.add_good_to_busket()
#     page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()