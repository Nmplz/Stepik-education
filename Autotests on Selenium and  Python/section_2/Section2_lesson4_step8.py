from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()

    find_x = browser.find_element(By.ID, "input_value")
    x = int(find_x.text)
    result = calc(x)

    answer_filed = browser.find_element(By.ID, "answer")
    answer_filed.send_keys(result)

    button = browser.find_element(By.ID, "solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
