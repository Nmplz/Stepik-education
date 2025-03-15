class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if len(self) != len(other):
            raise ArithmeticError("размерности векторов не совпадают")
        new_coord = []
        for i in range(len(self)):
            new_coord.append(self.coords[i] + other.coords[i])
        return Vector(*new_coord)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ArithmeticError("размерности векторов не совпадают")
        new_coord = []
        for i in range(len(self)):
            new_coord.append(self.coords[i] - other.coords[i])
        return Vector(*new_coord)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ArithmeticError("размерности векторов не совпадают")
        new_coord = []
        for i in range(len(self)):
            new_coord.append(self.coords[i] * other.coords[i])
        return Vector(*new_coord)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            return self + other
        new_coord = []
        for i in range(len(self)):
            new_coord.append(self.coords[i] + other)
        self.coords = tuple(new_coord)
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            return self - other
        new_coord = []
        for i in range(len(self)):
            new_coord.append(self.coords[i] - other)
        self.coords = tuple(new_coord)
        return self

    def __eq__(self, other):
        for i in range(len(self)):
            if not self.coords[i] == other.coords[i]:
                break
        else:
            return True
        return False
