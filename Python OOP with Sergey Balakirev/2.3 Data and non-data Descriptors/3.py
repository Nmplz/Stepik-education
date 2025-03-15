class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        for i in self.goods:
            if i.name == product.name:
                self.goods.remove(i)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, str) and self.min_length <= len(value) <= self.max_length:
            return setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, (float, int)) and 0 <= value <= self.max_value:
            return setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price
