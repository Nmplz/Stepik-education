class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.bag = []

    def is_posible_to_add(self, thing, delthing=0):
        if self.max_weight - self.current_weight >= thing.weight - delthing:
            return True
        else:
            False

    def add_thing(self, thing):
        if isinstance(thing, Thing) and self.is_posible_to_add(thing):
            self.bag.append(thing)
            self.current_weight += thing.weight
        else:
            raise ValueError("превышен суммарный вес предметов")

    def __len__(self):
        return len(self.bag)

    def __getitem__(self, item):
        if item < len(self):
            return self.bag[item]
        else:
            raise IndexError("неверный индекс")

    def __setitem__(self, key, value):
        if key < len(self):
            if self.is_posible_to_add(value, self.bag[key].weight):
                self.bag[key] = value
                self.current_weight += value.weight
            else:
                raise ValueError("превышен суммарный вес предметов")
        else:
            raise IndexError("неверный индекс")

    def __delitem__(self, key):
        if key < len(self):
            self.current_weight -= self.bag[key].weight
            del self.bag[key]
        else:
            raise IndexError("неверный индекс")


class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
