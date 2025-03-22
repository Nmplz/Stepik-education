from selenium.webdriver.common.by import By


# pytest -s -v --browser_name=chrome  .\Section3_lesson6_step7_Test_in_two_browsers_test.py
# pytest -s -v  .\Section3_lesson6_step7_Test_in_two_browsers_test.py
# pytest -v --tb=line --reruns 1 --browser_name=chrome .\Section3_lesson6_step7_Test_in_two_browsers_test.py

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
