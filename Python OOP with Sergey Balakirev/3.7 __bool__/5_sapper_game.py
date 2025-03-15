from random import randint


class GamePole:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE

    def __init__(self, N, M, total_mines):
        self.N = int(N)  # строки
        self.M = int(M)  # столбцы
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.M)] for i in range(self.N)]
        # self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):  # расставляет мины и делает все клетки закрытыми

        """Расставляем мины"""
        mines_counter = 0
        while mines_counter < self.total_mines:
            i = randint(0, self.N - 1)
            j = randint(0, self.M - 1)
            if not self.__pole_cells[i][j].is_mine:
                mines_counter += 1
                self.__pole_cells[i][j].is_mine = True

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        """Считаем мины вокруг клетки"""
        for x in range(self.N):
            for y in range(self.M):
                if not self.__pole_cells[x][y].is_mine:
                    mines = sum(self.__pole_cells[x + i][y + j].is_mine for i, j in indx if
                                0 <= x + i < self.N and 0 <= y + j < self.M)
                    self.__pole_cells[x][y].number = mines

    def open_cell(self, i, j):
        if 0 <= i < self.N and 0 <= j < self.M:
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError ()

    def show_pole(self):  # отображает игровое поле в консоли
        for row in self.__pole_cells:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*',
                       row))  ## (если клетка не открыта,
            # то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).


class Cell:
    def __init__(self):
        self.is_mine = False  # True - в клетке находится мина, False - мина отсутствует;
        self.number = 0  # число мин вокруг клетки
        self.is_open = False  # True - открыта; False - закрыта.

    def __bool__(self):
        return not self.is_open

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if isinstance(value, bool):
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and 0 <= value <= 9:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if isinstance(value, bool):
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

