from string import digits


class StringDigit(str):

    def __init__(self, value):
        self._str_check(value)
        self.value = value

    @staticmethod
    def _str_check(key):
        if not all(k in digits for k in key):  # Проверка на цифры
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self._str_check(self.value)
        self._str_check(other)
        return StringDigit(self.value + other)

    def __radd__(self, other):
        self._str_check(self)
        self._str_check(other)
        return StringDigit(other + self.value)
