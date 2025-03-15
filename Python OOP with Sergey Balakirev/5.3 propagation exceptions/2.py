class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string_):
        if len(self.chars) == 0:
            if (
                isinstance(string_, str)
                and self.min_length < len(string_) < self.max_length
            ):
                return True
            else:
                raise ValueError("недопустимая строка")

        if (
            isinstance(string_, str)
            and any(x in self.chars for x in string_)
            and self.min_length <= len(string_) <= self.max_length
        ):
            return True
        else:
            raise ValueError("недопустимая строка")


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):

        if len(request) != 2 or not (
            isinstance(request["login"], str) and isinstance(request["password"], str)
        ):
            raise TypeError("в запросе отсутствует логин или пароль")
        try:
            log_verified = self.login_validator.is_valid(request["login"])
            passwd_verified = self.password_validator.is_valid(request["password"])
        except Exception as e:
            raise ValueError(e)
        else:
            self._login = request["login"]
            self._password = request["password"]


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)

login, password = input().split()
try:
    lg.form({"login": login, "password": password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
