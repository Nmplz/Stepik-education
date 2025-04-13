from playwright.sync_api import Playwright, sync_playwright, expect
import time

#для запуска:  pytest --headed '.\Playwright Python\test_todo.py'

def test_add_todo(page) -> None:
    
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    time.sleep(2)




