def test_new_tab(page):

    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator(".nav-link", has_text="Sign out")
    assert sign_out.is_visible()
