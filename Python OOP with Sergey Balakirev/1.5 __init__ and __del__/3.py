import random


# здесь объявляйте класс Money
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

    def nullable(self):
        self.sp = (0, 0)
        self.ep = (0, 0)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


lst = [Line, Rect, Ellipse]
elements = [
    lst[random.randint(0, 2)](
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10),
    )
    for i in range(217)
]

# elements = [x.nullable() if isinstance(x, Line) else x for x in elements]
for i in elements:
    if isinstance(i, Line):
        i.nullable()
