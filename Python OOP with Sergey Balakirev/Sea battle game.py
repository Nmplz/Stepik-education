from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        x1, y1 = self.get_start_coords()
        x2, y2 = ship.get_start_coords()

        # Определим диапазон покрытия первого корабля
        ship1_area = set()
        if self._tp == 1:  # горизонтальный
            for i in range(self._length):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        ship1_area.add((x1 + i + dx, y1 + dy))
        else:  # вертикальный
            for i in range(self._length):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        ship1_area.add((x1 + dx, y1 + i + dy))

        # Проверим перекрытие второго корабля с зоной первого
        if ship._tp == 1:  # горизонтальный
            for i in range(ship._length):
                if (x2 + i, y2) in ship1_area:
                    return True
        else:  # вертикальный
            for i in range(ship._length):
                if (x2, y2 + i) in ship1_area:
                    return True

        return False

    def is_out_pole(self, size):
        if self._tp == 1:  # горизонтальный
            return not (
                0 <= self._x < size
                and 0 <= self._y < size
                and self._x + self._length - 1 < size
            )
        else:  # вертикальный
            return not (
                0 <= self._x < size
                and 0 <= self._y < size
                and self._y + self._length - 1 < size
            )

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        self._cells[indx] = value
        if 2 in self._cells:
            self._is_move = False


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        ships_to_create = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for length in ships_to_create:
            while True:
                ship = Ship(length, tp=randint(1, 2))
                ship.set_start_coords(
                    randint(0, self._size - 1), randint(0, self._size - 1)
                )
                if not self.is_collision(ship) and not ship.is_out_pole(self._size):
                    self._ships.append(ship)
                    break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            direction = randint(-1, 1)
            old_coords = ship.get_start_coords()
            ship.move(direction)
            if self.is_collision(ship) or ship.is_out_pole(self._size):
                ship.set_start_coords(*old_coords)

    def is_collision(self, new_ship):
        for ship in self._ships:
            if ship.is_collide(new_ship):
                return True
        return False

    def get_pole(self):
        pole = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for i in range(ship._length):
                if ship._tp == 1:
                    pole[y][x + i] = ship[i]
                else:
                    pole[y + i][x] = ship[i]
        return tuple(tuple(row) for row in pole)

    def show(self):
        pole = self.get_pole()
        for row in pole:
            print(" ".join(map(str, row)))
