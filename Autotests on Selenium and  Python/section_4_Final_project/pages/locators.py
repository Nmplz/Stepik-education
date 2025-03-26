from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кортеж, который нужно распаковать ('css selector', '#registration_link')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


##TODO  СДЕЛАТЬ ПРОВЕРКУ НА ФОРМУ ЛОГИНА А НЕ НА ПОЛЯ И КНОПКИ


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
