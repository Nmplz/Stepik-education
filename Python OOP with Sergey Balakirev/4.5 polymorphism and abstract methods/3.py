class Validator:
    def _is_valid(self, data):
        raise NotImplementedError("в классе не переопределен метод _is_valid")


class StringValidator(Validator):
    pass


class IntegerValidator(Validator):
    pass


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if isinstance(value, float):
            return self._is_valid(value)
        return False

    def _is_valid(self, data):
        return self.min_value <= data <= self.max_value
