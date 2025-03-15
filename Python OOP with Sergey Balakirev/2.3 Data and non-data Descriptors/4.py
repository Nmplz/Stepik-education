class Bag:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.curr_weight = 0.0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.curr_weight + thing.weight <= self.max_weight:
            self.__things.append(thing)
            self.curr_weight += thing.weight

    def remove_thing(self, indx):
        if indx < len(self.__things):
            self.curr_weight -= self.__things[indx].weight
            del self.__things[indx]

    def get_total_weight(self):
        return self.curr_weight


class Thing:

    def __init__(self, name, weight):
        if isinstance(name, str) and isinstance(weight, (float, int)):
            self.name = name
            self.weight = weight
