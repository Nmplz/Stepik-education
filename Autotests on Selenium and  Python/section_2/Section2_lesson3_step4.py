from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    jorney_button = browser.find_element(By.CLASS_NAME, "btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    find_x = browser.find_element(By.ID, "input_value")
    answer = calc(find_x.text)

    form_field = browser.find_element(By.ID, "answer")
    form_field.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
