from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BUSKET_LINK)
        link.click()

    # How- как искать (css, id, xpath и тд)
    # What-  собственно что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    """
        is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 

        is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    """

    # метод, который проверяет, что элемент появляется на странице в течение заданного времени
    def is_element_appear(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not,
    # в зависимости от того, какой результат мы ожидаем:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_with_text_present(self, how, what, text):
        try:
            elements = self.browser.find_elements(how, what)
            for element in elements:
                if element.text == text:
                    return True
            raise Exception(f"There is No such element '{what}' with text '{text}'")
        except NoSuchElementException:
            return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," " probably unauthorised user"
