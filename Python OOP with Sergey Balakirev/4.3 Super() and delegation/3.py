class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name):
        self.name = name
        self.sell_obj = []

    def add_object(self, obj):
        if isinstance(obj, (Flat, Land, House)):
            self.sell_obj.append(obj)

    def remove_object(self, obj):
        if obj in self.sell_obj:
            self.sell_obj.remove(obj)

    def get_objects(self):
        return self.sell_obj
