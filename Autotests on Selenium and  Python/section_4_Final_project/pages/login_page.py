from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        expected_url = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form field is not presented"

    def register_new_user(self, email: str, password: str):

        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email_field.send_keys(email)

        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password_field.send_keys(password)

        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_confirm_password_field.send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def is_user_registred(self):
        success_element_text = self.browser.find_element(*LoginPageLocators.SUCCESS_REGISTER_MESSAGE).text
        print(success_element_text)
        assert success_element_text == "Thanks for registering!", "Registration was unsuccesful, message not appear"
