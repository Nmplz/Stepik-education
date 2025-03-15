class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        # Проверка, что string - это строка и её длина в пределах min_length и max_length
        return (
            isinstance(string, str)
            and self.min_length <= len(string) <= self.max_length
        )


class StringValue:
    validator = ValidateString()

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # Проверка валидности значения через валидатор
        if self.validator.validate(value):
            setattr(instance, self.name, value)
        else:
            False


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        return print(
            f"<form>\n Логин: {self.login}\n Пароль: {self.password} \n Email: {self.email} \n </form>"
        )
