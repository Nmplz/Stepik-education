import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# Browser --incognito


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--incognito")  # Включаем режим инкогнито
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser

    browser.quit()


# TODO Можно сделать через Класс, можно просто в строчку.


@pytest.fixture(scope="session")
def load_credentials():
    with open("D:\stepic_Cred.json", "r") as file:
        credentials = json.load(file)
        return credentials


class TestLogin:
    def test_autorization(self, browser, load_credentials):
        login = load_credentials["login_stepik"]
        password = load_credentials["password_stepik"]

        browser.get("https://stepik.org/lesson/236895/step/1")

        login_button = browser.find_element(By.ID, "ember466")
        login_button.click()
        login_form_email = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
        login_form_email.send_keys(login)
        login_form_passwd = browser.find_element(
            By.CSS_SELECTOR, 'input[name="password"]'
        )
        login_form_passwd.send_keys(password)
        bottun_enter = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        bottun_enter.click()

        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element((By.ID, "ember527"))
        )

        stepik_lessons = [
            "https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1",
        ]
        list_of_errors = []
        for lesson in stepik_lessons:
            browser.get(lesson)
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "submit-submission"))
            )

            answer_field = browser.find_element(
                By.CSS_SELECTOR,
                ".ember-text-area.ember-view.textarea.string-quiz__textarea",
            )
            answer = math.log(int(time.time()))
            answer_field.send_keys(str(answer))
            send_button = browser.find_element(By.CLASS_NAME, "submit-submission")
            send_button.click()

            answer_hint = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
            answer_hint_text = answer_hint.text
            try:
                assert (
                    answer_hint_text == "Correct!"
                ), f"Answer incorrect! -> {answer_hint_text}"
            except AssertionError as e:
                print(f"Тест на {lesson} провален: {e}")
                list_of_errors.append(answer_hint_text)
        else:
            print(list_of_errors)
