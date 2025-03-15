from random import randint


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_human_win
        self.is_computer_win

    def _pole_checker(self, indx):
        r, c = indx
        if not (0 <= r < 3 and 0 <= c < 3):
            raise IndexError("некорректно указанные индексы")

    def __getitem__(self, item):
        self._pole_checker(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value_):
        self._pole_checker(key)
        r, c = key
        self.pole[r][c].value = value_

    def init(self):
        for x in self.pole:
            for i in x:
                i.value = 0

    def show(self):
        for row in self.pole:
            print(" | ".join(str(cell.value) for cell in row))
            print("-" * 9)

    def human_go(self):
        r, c = map(int, input("Введите две цифры через пробел от 0 до 2").split())
        if self.pole[r][c].value == self.FREE_CELL:
            self.pole[r][c].value = self.HUMAN_X

    def computer_go(self):
        while True:
            r = randint(0, 2)
            c = randint(0, 2)
            if self.pole[r][c].value == self.FREE_CELL:
                self.pole[r][c].value = self.COMPUTER_O
                break

    @property
    def is_human_win(self):
        if any(
            all(self.pole[x][y].value == self.HUMAN_X for y in range(3))
            for x in range(3)
        ):  # строки
            return True
        elif any(
            all(self.pole[y][x].value == self.HUMAN_X for y in range(3))
            for x in range(3)
        ):  # колонки
            return True
        elif all(self.pole[x][x].value == self.HUMAN_X for x in range(3)) or all(
            self.pole[x][2 - x].value == self.HUMAN_X for x in range(3)
        ):  # диагонали
            return True
        else:
            return False

    @property
    def is_computer_win(self):
        if any(
            all(self.pole[x][y].value == self.COMPUTER_O for y in range(3))
            for x in range(3)
        ):  # строки
            return True
        elif any(
            all(self.pole[y][x].value == self.COMPUTER_O for y in range(3))
            for x in range(3)
        ):  # колонки
            return True
        elif all(self.pole[x][x].value == self.COMPUTER_O for x in range(3)) or all(
            self.pole[x][2 - x].value == self.COMPUTER_O for x in range(3)
        ):  # диагонали
            return True
        else:
            return False

    @property
    def is_draw(self):
        if self.is_human_win or self.is_computer_win:
            return False
        return all(
            self.pole[x][y].value != self.FREE_CELL for x in range(3) for y in range(3)
        )

    def __bool__(self):
        if all(
            [
                self.pole[x][y].value != self.FREE_CELL
                for x in range(3)
                for y in range(3)
            ]
        ):
            return False
        return True


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value != 0:
            return False
        return True
