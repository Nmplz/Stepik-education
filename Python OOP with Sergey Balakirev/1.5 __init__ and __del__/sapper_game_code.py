from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N  # длинна поля
        self._m = M  # Количество мин
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True
                m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum(
                        (self.pole[x + i][y + j].mine for i, j in indx if 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(* map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


# (если клетка не открыта, то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).


pole_game = GamePole(10, 12)
