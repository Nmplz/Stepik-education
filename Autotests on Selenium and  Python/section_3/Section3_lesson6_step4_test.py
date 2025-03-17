import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Browser --incognito


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--incognito")  # Включаем режим инкогнито

    browser = webdriver.Chrome(options=options)
    yield browser

    browser.quit()


# TODO Можно сделать через Класс, можно просто в строчку.
