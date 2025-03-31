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
        assert book_name in added_book_name, f"Expected book name -{book_name}. But we got {added_book_name}"

    def added_good_price_check(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER_ADD_TO_BUSKET).text
        assert book_price in added_book_price, f"Expected book price -{book_price}. But we got {added_book_price}"
