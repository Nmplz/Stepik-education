# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# # # -v - выводит отчет более подробно
# # #-s - показывает в консоли выводы print'ов.
# # # "--tb=line", чтобы сократить лог с результатами теста


# # parser.addoption("--browser_name", ...) — добавляет новый аргумент --browser_name, который можно передавать при запуске pytest.
# # action="store" — сохраняет переданное пользователем значение (например, "chrome" или "firefox")
# # default=None — если аргумент не передан, его значение будет None.


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name",
#         action="store",
#         default=None,
#         help="Choose browser: chrome or firefox",
#     )


# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
