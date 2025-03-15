class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        """•	__lt__(self, other) — <;
•	__le__(self, other) — <=;
•	__eq__(self, other) — ==;
•	__ne__(self, other) — !=;
•	__gt__(self, other) — >;
•	__ge__(self, other) — >=.
"""

    @staticmethod
    def vols(obj):
        return obj.__a * obj.__b * obj.__c

    def __le__(self, other):
        return self.vols(self) <= other.vols(other)

    def __lt__(self, other):
        return self.vols(self) < other.vols(other)

    @classmethod
    def dimen_chec(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.dimen_chec(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.dimen_chec(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.dimen_chec(value):
            self.__c = value


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem("кеды", 1024, Dimensions(40, 30, 120))
umbrella = ShopItem("зонт", 500.24, Dimensions(10, 20, 50))
fridge = ShopItem("холодильник", 40000, Dimensions(2000, 600, 500))
chair = ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
