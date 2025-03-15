import time


class Discriptor:

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not hasattr(instance, self.name):
            setattr(instance, self.name, value)


class Mechanical:
    date = Discriptor()

    def __init__(self, date):
        self.date = date


class Aragon:
    date = Discriptor()

    def __init__(self, date):
        self.date = date


class Calcium:
    date = Discriptor()

    def __init__(self, date):
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100
    d = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if self.d[slot_num] == type(filter) and self.slots[slot_num - 1] is None:
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all(
            [
                i != None and 0 <= time.time() - i.date <= self.MAX_DATE_FILTER
                for i in self.slots
            ]
        )
