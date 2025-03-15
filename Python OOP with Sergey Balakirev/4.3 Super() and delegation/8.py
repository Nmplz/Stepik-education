class ItemAttrs:

    def __getitem__(self, item):
        key = list(self.__dict__)[item]
        return self.__dict__[key]

    def __setitem__(self, key, value):
        key_ = list(self.__dict__)[key]
        self.__dict__[key_] = value


class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y
