from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Alert
# Confirm
# Prompt


try:
    browser = webdriver.Chrome()

    """
    browser.switch_to.window(new_window) # В аргумент указываем вкладку на которую хотим перейти.

    new_window = browser.window_handles[1] #window_handles - возвращает массив имён всех вкладок, наша вторая, поэтому [1]
    first_window = browser.window_handles[0] #можем запомнить имя текущей вкладки

    """

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
