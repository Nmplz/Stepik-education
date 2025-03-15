class Validator:
    def _is_valid(self, data):
        pass

    def __call__(self, *args, **kwargs):
        if self._is_valid(*args, **kwargs):
            return True
        else:
            raise ValueError("данные не прошли валидацию")


class IntegerValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == int and self.min_value <= data <= self.max_value:
            return True
        return False


class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float and self.min_value <= data <= self.max_value:
            return True
        return False
