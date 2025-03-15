class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        for i in self.goods:
            if i.name == product.name:
                self.goods.remove(product)


class Product:
    id = 0

    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self, name, weight, price):
        self.id = self.get_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif (
            key in ["weight", "price"] and isinstance(value, (int, float)) and value > 0
        ):
            object.__setattr__(self, key, value)
        elif key == "id" and isinstance(value, int):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)
