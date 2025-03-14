class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        new = super().__new__(Point)
        new.__dict__.update(self.__dict__)
        return new


pt = Point(5, 7)
pt_clone = pt.clone()
