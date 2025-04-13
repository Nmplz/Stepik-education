"""
<select class="form-select" id="floatingSelect" aria-label="Floating label select example">
    <option value="1">Нашел и завел bug</option>
    <option value="2">Предложил новую функцию</option>
    <option value="3">У меня лапки</option>
  </select>
"""


def test_select(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#floatingSelect", value="3")
    page.select_option("#floatingSelect", index=1)
    page.select_option("#floatingSelect", label="Нашел и завел bug")
