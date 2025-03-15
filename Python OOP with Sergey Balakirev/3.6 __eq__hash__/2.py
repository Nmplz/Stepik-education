import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {}

for i in lst_in:
    name, weight_price = i.split(":")
    weight, price = weight_price.split()
    key = ShopItem(name, weight, price)
    if key in shop_items:
        shop_items[key][1] += 1
    else:
        shop_items[key] = [key, 1]
