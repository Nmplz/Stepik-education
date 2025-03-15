class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        if isinstance(indx, int) and indx < len(self.items):
            for i, v in enumerate(self.items):
                if i == indx:
                    self.items.remove(self.items[i])

    def get_items(self):
        return [x.money for x in self.items]


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            self.money = self.money + other.money
        if isinstance(other, int):
            self.money = self.money + other
        return self.money

    def __radd__(self, other):
        return self + other
