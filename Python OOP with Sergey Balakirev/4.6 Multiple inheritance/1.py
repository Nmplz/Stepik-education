class Digit:

    def _check_value(self, value, types=(int, float), fltr=lambda x: True) -> None:
        if not isinstance(value, types):
            raise ValueError("значение не может быть отрицательным")

    def __init__(self, value) -> None:
        self._check_value(value)
        self.value = value


class Integer(Digit):
    def __init__(self, value) -> None:
        self._check_value(value, types=(int,))
        super().__init__(value)


class Float(Digit):
    def __init__(self, value) -> None:
        self._check_value(value, types=(float,))


class Positive(Digit):
    def __init__(self, value) -> None:
        self._check_value(value, fltr=lambda x: x > 0)
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value) -> None:
        self._check_value(value, fltr=lambda x: x < 0)
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value) -> None:
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value) -> None:
        super().__init__(value)


digits = [
    PrimeNumber(3),
    PrimeNumber(1),
    PrimeNumber(4),
    FloatPositive(1.5),
    FloatPositive(9.2),
    FloatPositive(6.5),
    FloatPositive(3.5),
    FloatPositive(8.9),
]

lst_positive = filter(lambda x: isinstance(x, Positive), digits)
lst_float = filter(lambda x: isinstance(x, Float), digits)
