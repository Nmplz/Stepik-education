#pytest -s -v  --headed '.\test_4_radio_checkBox_switch.py' --slowmo 1000

def test_checkbox(page):

    page.goto("https://zimaev.github.io/checks-radios/")
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()
