class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        if isinstance(gd, (Cup, Notebook, TV, Table)):
            self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{good.name}:{good.price}" for good in self.goods]


tv1 = TV("XXX", 300)
tv2 = TV("Samsung", 500)
table = Table("Столик", 40)
notebook1 = Notebook("Accer", 220)
notebook2 = Notebook("Lenovo", 100)
cup1 = Cup("Кружечка", 10)
cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(notebook1)
cart.add(notebook2)
cart.add(cup1)
