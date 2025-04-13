def test_check_radio(page):

    page.goto("https://zimaev.github.io/checks-radios/")
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()


def test_check_radio2(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()
