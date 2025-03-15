class Money:
    def __init__(self, volume=0):
        self.volume = volume
        self.cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, link):
        self.__cb = link

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def curr_exchange(self, curr):
        try:
            if isinstance(curr, MoneyR):
                return round(curr.volume, 2)
            elif isinstance(curr, MoneyD):
                res = curr.volume * self.cb["rub"]
                return round(res, 2)
            elif isinstance(curr, MoneyE):
                res = curr.volume * self.cb["euro"] * self.cb["rub"]
                return round(res, 2)
        except:
            raise ValueError("Неизвестен курс валют.")

    def __lt__(self, other):  # <
        return self.curr_exchange(self) < other.curr_exchange(other)

    def __le__(self, other):  # <=
        return self.curr_exchange(self) <= other.curr_exchange(other)

    def __eq__(self, other):  # ==
        # print(self.curr_exchange(self), other.curr_exchange(other))
        return round(self.curr_exchange(self)) == round(other.curr_exchange(other))


class MoneyR(Money):
    pass


class MoneyD(Money):
    pass


class MoneyE(Money):
    pass


class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

    @classmethod
    def register(cls, money):
        money.cb = cls.rates
