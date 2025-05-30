import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pytest -s -v test_fixture7.py
# -v - выводит отчет более подробно
# -s - показывает в консоли выводы print'ов.
# --tb=line -  указывает, что нужно выводить только одну строку из лога каждого упавшего теста


# Использую Constest.py

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
