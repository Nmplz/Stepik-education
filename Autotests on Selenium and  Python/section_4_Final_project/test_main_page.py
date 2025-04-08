import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:  # не забываем передать первым аргументом self

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.new
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"

        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        busket_page = BasketPage(browser, link)
        busket_page.busket_not_empty_on_first_logon()
        busket_page.is_busket_empty()


# Гость открывает главную страницу
# Переходит в корзину по кнопке в шапке сайта
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста
