class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float or self.min_value > value or self.max_value < value:
            raise ValueError("значение не прошло валидацию")


class IntegerValidator(FloatValidator):
    def __call__(self, value):
        if type(value) != int or self.min_value > value or self.max_value < value:
            raise ValueError("значение не прошло валидацию")


def is_valid(lst, validators):
    new_lst = []
    for i in lst:
        for validator in validators:
            try:
                validator(i)
                new_lst.append(i)
            except:
                pass
    return new_lst




