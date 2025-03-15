class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.is_valid(a, b, c)

    @staticmethod
    def is_valid(a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("из указанных длин сторон нельзя составить треугольник")

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("стороны треугольника должны быть положительными числами")
        return super().__setattr__(name, value)


input_data = [
    (1.0, 4.54, 3),
    ("abc", 1, 2, 3),
    (-3, 3, 5.2),
    (4.2, 5.7, 8.7),
    (True, 3, 5),
    (7, 4, 6),
]
lst_tr = []

for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        continue
