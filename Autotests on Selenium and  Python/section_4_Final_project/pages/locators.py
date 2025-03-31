from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кортеж, который нужно распаковать ('css selector', '#registration_link')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:

    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class ='price_color']")
    ADD_TO_BUSKET_BUTTOM = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_WICH_ADDED_TO_BUSKET_SUCCESFULLY = (By.XPATH, 
    '//div[@class="alertinner "][contains(., " has been added to your basket.")]')
    PRODUCT_PRICE_AFTER_ADD_TO_BUSKET= (By.XPATH, 
    '//div[@class="alertinner "][contains(., "View basket")]')