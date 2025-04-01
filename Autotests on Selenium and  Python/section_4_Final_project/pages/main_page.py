from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class MainPage(BasePage):

    ## Можно просто pass
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
