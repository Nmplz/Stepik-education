class ShopInterface:
    def get_id(self):
        raise NotImplementedError("в классе не переопределен метод get_id")


class ShopItem(ShopInterface):
    __ID = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.set_id()

    @classmethod
    def set_id(cls):
        cls.__ID += 1
        return cls.__ID

    def get_id(self):
        return self.__id
