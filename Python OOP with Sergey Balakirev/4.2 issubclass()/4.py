class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))
