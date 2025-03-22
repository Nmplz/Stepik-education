import pytest
from selenium.webdriver.common.by import By


class TestMultipleLanguage:

    def test_add_to_basket(self, browser):

        browser.get(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        )

        try:

            add_to_busket_botton = browser.find_element(
                By.CSS_SELECTOR, ".btn-add-to-basket"
            )

            assert add_to_busket_botton.is_displayed(), "Add to basket button not found"

        except Exception:
            pytest.fail("Basket button not found on page")
