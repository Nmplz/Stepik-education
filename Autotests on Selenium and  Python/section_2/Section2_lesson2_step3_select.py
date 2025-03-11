from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# .find_element
# .text
# Select
# .select_by_value

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_digit1 = browser.find_element(By.ID, "num1")
    digit_1 = int(find_digit1.text)
    find_digit2 = browser.find_element(By.ID, "num2")
    digit_2 = int(find_digit2.text)
    summ = str(digit_1 + digit_2)

    select = Select(browser.find_element(By.CSS_SELECTOR, 'select[id="dropdown"]'))
    select.select_by_value(summ)
    find_submit =browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default').click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
