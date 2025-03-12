from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Alert
# Confirm
# Prompt



try:
    browser = webdriver.Chrome()

    #ALERT
    browser.execute_script("alert('Hello!');") # Вызываем алерт
    alert = browser.switch_to.alert            # Переключаемся на окно с алертом
    time.sleep(2)
    alert.accept()                             # Принимаем "OK"
    
    
    browser.execute_script("alert('Hello!');") # Вызываем алерт
    alert = browser.switch_to.alert            # Переключаемся на окно с алертом
    alert_text = alert.text                    # Получаем текст из Алерта
    time.sleep(2)
    alert.accept()
    
    #CONFIRM
    browser.execute_script("confirm('Hello! I am CONFIRM');") # Вызываем Confirm  с кнопками "Отмена" "ОК"
    confirm  = browser.switch_to.alert           # Переключаемся на окно с Confirm
    time.sleep(2)
    confirm.accept()                             # Получаем текст из Confirm
    #confirm.dismiss()                           #Для отказа


    #PROMPT
    browser.execute_script("prompt('Hello! I am PROMT');")
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    time.sleep(2)
    prompt.accept()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
