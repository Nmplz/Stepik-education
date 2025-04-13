# По умолчанию диалоговые окна  автоматически закрываются Playwright, поэтому вам необязательно их обрабатывать.
def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()


# dialog.accept() - закрыть диалоговое окно нажав кнопку «OK»
# dialog.default_value - возвращает значение подсказки по умолчанию, в случае если тип диалога prompt
# dialog.dismiss() - закрыть диалоговое окно нажав кнопку «Отмена/Cancel»
# dialog.message - возвращает сообщение отображаемое в диалоговом окне.
# dialog.type - возвращает тип диалогового окна


# «Диалог Confirmation» >> Нажимаем OK
def test_dialogs_confirmation_ok(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()


# «Диалог Confirmation» >> Нажимаем Отмена
def test_dialogs_confirmation_cancel(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_text("Диалог Confirmation").click()
