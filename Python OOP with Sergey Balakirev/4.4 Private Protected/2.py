class Furniture:
    def __init__(self, name, weight):
        # self.__verify_name(name)
        # self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(value)
        if key == "_weight":
            self.__verify_weight(value)
        super().__setattr__(key, value)

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError("название должно быть строкой")

    def __verify_weight(self, val):
        if not isinstance(val, (int, float)) or val <= 0:
            raise TypeError("вес должен быть положительным числом")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.values())

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value
