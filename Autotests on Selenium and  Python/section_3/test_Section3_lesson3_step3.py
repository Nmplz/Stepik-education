import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_guest_should_see_login_link(browser):
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element(
        By.CSS_SELECTOR, "[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, "[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("ivan.petrov@example.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text


def test_guest_should_see_login_link_fail(browser):
    browser.get("http://suninjuly.github.io/registration2.html")
    input1 = browser.find_element(
        By.CSS_SELECTOR, "[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, "[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("ivan.petrov@example.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
