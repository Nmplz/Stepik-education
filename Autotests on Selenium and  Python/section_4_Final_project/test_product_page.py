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


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket_button()
    page.add_good_to_busket()
    page.solve_quiz_and_get_code()
    page.added_good_name_check()
    page.added_good_price_check()

