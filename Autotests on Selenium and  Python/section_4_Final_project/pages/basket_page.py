from .locators import BusketLocators
from .base_page import BasePage


class BasketPage(BasePage):

    # Позитивную - проверяет текст что корзина пуста.
    # Негативную - проверяет что в корзине нет товара, и если он есть, написать осмысленное сообщение ассерта.

    def is_busket_empty(self):
        busket_current_state = self.browser.find_element(*BusketLocators.BUSKET_EMPTY).text
        print(busket_current_state)
        assert busket_current_state == "Your basket is empty. Continue shopping", "Busket should be empty"

    def busket_not_empty_on_first_logon(self):
        goods_in_busket_are_present = self.is_not_element_present(*BusketLocators.BUSKET_SUMMARY, 2)
        assert goods_in_busket_are_present, "Корзина не пуста. Локатор товаров в корзине обнаружен, хотя не должен присутствовать на странице"
