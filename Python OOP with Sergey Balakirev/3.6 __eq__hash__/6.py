from math import sqrt


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами"
            )
        setattr(instance, self.name, value)


class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return all([a < b + c, b < a + c, c < a + b])
        return True

    def __setattr__(self, key, value):
        if (
            (key == "a" and not self.__is_triangle(value, self.b, self.c))
            or (key == "b" and not self.__is_triangle(self.a, value, self.c))
            or (key == "c" and not self.__is_triangle(self.a, self.b, value))
        ):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) / 2
        a, b, c = self.a, self.b, self.c
        return sqrt(p * (p - a) * (p - b) * (p - c))
