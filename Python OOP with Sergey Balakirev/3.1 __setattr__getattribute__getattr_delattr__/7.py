class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, att):
        self.__a = att

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, att):
        self.__b = att

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, att):
        self.__c = att

    def __setattr__(self, key, value):
        if key == "MIN_DIMENSION" or key == "MAX_DIMENSION":
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )

        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == "MIN_DIMENSION" or item == "MAX_DIMENSION":
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        else:
            super().__delattr__(item)
