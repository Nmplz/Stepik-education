class Box3D:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_attr(self):
        return (self.width, self.height, self.depth)

    def __add__(self, other):
        return type(self)(*map(sum, zip(self.get_attr(), other.get_attr())))

    def __mul__(self, other):
        return type(self)(*map(lambda x: x * other, self.get_attr()))

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return type(self)(
                *map(lambda x, y: x - y, self.get_attr(), other.get_attr())
            )  ##

    def __floordiv__(self, other):
        if isinstance(other, int) and other != 0:
            return type(self)(*[x // other for x in self.get_attr()])
        raise ZeroDivisionError("ZeroDivisionError")

    def __mod__(self, other):
        if isinstance(other, int) and other != 0:
            return type(self)(*[x % other for x in self.get_attr()])
        raise ZeroDivisionError("ZeroDivisionError")
