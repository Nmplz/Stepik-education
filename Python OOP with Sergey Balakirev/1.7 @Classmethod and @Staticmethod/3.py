import string
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if len(number) == 19:
            return all(
                map(
                    lambda x: x in string.digits,
                    [x for i in number.split("-") for x in i],
                )
            )
        return False

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2:
            return all(
                map(
                    lambda x: x in cls.CHARS_FOR_NAME,
                    [x for i in name.split() for x in i],
                )
            )
        return False
