import string
from random import randint


class EmailValidator:
    SIMBOLS = string.ascii_letters + string.digits + "._"

    @classmethod
    def get_simbol(cls):
        return cls.SIMBOLS[randint(0, len(cls.SIMBOLS))]

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email_len = randint(5, 10)
        mail = [cls.get_simbol() for x in range(email_len)]
        return "".join(mail) + "@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email) or email.count("@") > 1:
            return False
        head, tail = email.split("@")
        if 0 < len(head) < 101 and len(tail) < 51 and 0 < tail.count(".") < 2:
            if tail.count("..") > 0 or head.count("..") > 0:
                return False
            for i in email:
                if i not in (cls.SIMBOLS + "@"):
                    break
            else:
                return True
            return False
        return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
