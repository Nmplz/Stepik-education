from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.

    def should_be_add_to_busket_button(self):

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSKET_BUTTOM)

    def add_good_to_busket(self):

        busket_buttom = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTOM)
        busket_buttom.click()
        

    def added_good_name_check(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_WICH_ADDED_TO_BUSKET_SUCCESFULLY).text
        assert book_name == added_book_name, f"Expected book name -{book_name}. But we got {added_book_name}"

    def added_good_price_check(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER_ADD_TO_BUSKET).text
        assert book_price == added_book_price, f"Expected book price >{book_price}<. But we got >{added_book_price}<"

    def should_not_be_success_message(self):
        #проверяет отсутствие сообщения об успехе на странице на данный момент
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), "Success message shouldn't appear"

    def should_dissapear_of_success_message (self):
         # проверяет, что сообщение исчезает.
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE),"Success message DO NOT  dissappear after 4 sec"