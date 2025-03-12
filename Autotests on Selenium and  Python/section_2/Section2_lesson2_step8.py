from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

# .find_element
# .send_keys
# os.path.abspath
# os.path.join

link = "https://suninjuly.github.io/file_input.html"
# получаем путь к директории текущего исполняемого
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, "Section2_lesson2_step8_file_to_download.txt")


try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname_field = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter first name"]'
    )
    firstname_field.send_keys("Alexandr")
    lastname_field = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter last name"]'
    )
    lastname_field.send_keys("Nmplz")
    lastname_field = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter email"]'
    )
    lastname_field.send_keys("mail@gmail.com")
    add_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    add_file.send_keys(file_path)  ##  Add file in site form
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
