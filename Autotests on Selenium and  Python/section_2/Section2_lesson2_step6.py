from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


# .find_element
# .send_keys
# .execute_script


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_x = browser.find_element(By.ID, "input_value")
    x = int(find_x.text)
    y = calc(x)
    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    robotRule_radio = browser.find_element(By.ID, "robotsRule").click()
    button.click()  # Нажимаем сабмит

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
