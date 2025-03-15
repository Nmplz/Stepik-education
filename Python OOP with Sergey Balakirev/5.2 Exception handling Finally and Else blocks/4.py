class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.left = self._x
        self.right = self._x + self._width
        self.up = self._y + self._height
        self.bottom = self._y

    def __setattr__(self, key, value):
        if key in ["_x", "_y"]:
            if isinstance(value, (int, float)):
                super().__setattr__(key, value)
            else:
                raise ValueError("некорректные координаты и параметры прямоугольника")

        elif key in ["_width", "_height"]:
            if isinstance(value, (int, float)) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("некорректные координаты и параметры прямоугольника")

        else:
            super().__setattr__(key, value)

    def is_collision(self, rect):
        if (
            self.right < rect.left
            or self.left > rect.right
            or self.up < rect.bottom
            or self.bottom > rect.up
        ):
            return False  # Нет коллизии
        raise TypeError("прямоугольники пересекаются")  # Коллизия есть


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []

for x in lst_rect:
    collision_found = False
    for y in lst_rect:
        if x != y:
            try:
                x.is_collision(y)
            except TypeError:
                collision_found = True
                break
    if not collision_found:
        lst_not_collision.append(x)
