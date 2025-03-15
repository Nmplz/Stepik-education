class Test:
    def __init__(self, descr):
        self.descr = self.descr_check(descr)

    def descr_check(self, item):
        if type(item) is str:
            if 10 < len(item) < 10000:
                return item
            else:
                raise ValueError(
                    "формулировка теста должна быть от 10 до 10 000 символов"
                )
        else:
            raise ValueError("формулировка теста должна быть от 10 до 10 000 символов")

    # def __setattr__(self, key, value):
    #     if key == 'descr':
    #         if type(value) is str:
    #             if 10 < len(value) < 10000:
    #                 super().__setattr__(key, value)
    #             else:
    #                 raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
    #         else:
    #             raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
    #     else:
    #         super().__setattr__(key, value)

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key == "max_error_digit" and not value >= 0:
            raise ValueError("недопустимые значения аргументов теста")
        elif key == "ans_digit" and not isinstance(value, (float, int)):
            raise ValueError("недопустимые значения аргументов теста")
        else:
            super().__setattr__(key, value)

    def run(self):
        ans = float(input())
        if abs(ans - self.ans_digit) <= self.max_error_digit:
            return True
        return False


descr, ans = map(str.strip, input().split("|"))

try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)
