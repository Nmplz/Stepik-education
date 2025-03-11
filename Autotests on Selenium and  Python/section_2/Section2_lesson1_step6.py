from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    treasure_value = x_element.get_attribute("valuex")
    print(treasure_value)
    y = calc(treasure_value)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
