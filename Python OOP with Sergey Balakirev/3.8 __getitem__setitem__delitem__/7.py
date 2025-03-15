class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for x in self.pole:
            for i in x:
                i.is_free = True
                i.value = 0

    def cell_cheker(self, item):
        if type(item) != tuple or len(item) != 2:
            raise IndexError("неверный индекс клетки")
        if any(not (0 <= x < 3) for x in item if type(x) != slice):
            raise IndexError("неверный индекс клетки")

    def __getitem__(self, item):
        self.cell_cheker(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))
        return self.pole[r][c].value

    def __setitem__(self, key, value_):
        r, c = key
        self.cell_cheker(key)
        if self.pole[r][c]:
            self.pole[r][c].value = value_
            self.pole[r][c].is_free = False
        else:
            raise ValueError("клетка уже занята")


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free
