from math import sqrt


class RadiusVector:

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            for i in range(args[0]):
                setattr(self, f"vector{i}", 0)
        else:
            for i, v in enumerate(args):
                setattr(self, f"vector{i}", v)

    def __len__(self):
        return len(self.__dict__)

    def __abs__(self):
        coords = self.get_coords()
        result = 0
        for x in coords:
            result += x**2
        return sqrt(result)

    def set_coords(self, *args):
        for i, v in enumerate(args):
            if len(self) > i:
                setattr(self, f"vector{i}", v)

    def get_coords(self):
        return tuple([self.__dict__[i] for i in self.__dict__])
