from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# .execute_script


try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")  # выполнение скрипта в кавычках
    # если в сприкте нужны ''
    browser.execute_script('document.title="Script executing";')

    # можно передать инструкции по очереди
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
