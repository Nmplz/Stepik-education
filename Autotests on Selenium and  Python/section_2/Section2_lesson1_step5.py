from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute(
        "checked"
    )  # возвращает True или False в зависимости от того, выбран ли радиокнопка
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("value of robot radio: ", robot_checked)
    assert robot_checked is None, "Robot radio is selected by default"
    time.sleep(10)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submin_disabled = submit_button.get_attribute("disabled")
    print("value of submit button: ", submin_disabled)
    assert submin_disabled == "true", "Submit button is not disabled"

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
