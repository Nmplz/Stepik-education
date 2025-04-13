import time


def test_checkbox(page):

    page.goto("https://zimaev.github.io/checks-radios/")
    page.locator("text=Default checkbox").check()
    time.sleep(0.5)
    page.locator("text=Checked checkbox").check()
    time.sleep(0.5)
    page.locator("text=Default radio").check()
    time.sleep(0.5)
    page.locator("text=Default checked radio").check()
    time.sleep(0.5)
    page.locator("text=Checked switch checkbox input").check()
