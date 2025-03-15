from copy import deepcopy


class Box:

    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self.curr_weight = 0
        self._things = []

    def add_thing(self, obj):
        if self._max_weight < self.curr_weight + obj[1]:
            raise ValueError("превышен суммарный вес вещей")
        self._things.append(obj)
        self.curr_weight += obj[1]


class BoxDefender:
    def __init__(self, b):
        self.__box = b
        self.__things_copy = deepcopy(b._things)

    def __enter__(self):
        return self.__box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__box._things = self.__things_copy
        return False
