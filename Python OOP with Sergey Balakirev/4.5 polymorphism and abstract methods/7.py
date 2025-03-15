class Track:
    def __init__(self, *args):
        self.__points = []

        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            # Если два аргумента и они числовые, создать объект PointTrack
            x, y = args
            self.__points.append(PointTrack(x, y))
        else:
            # Если передаются объекты PointTrack
            for v in args:
                if isinstance(v, PointTrack):
                    self.__points.append(v)  # Добавляем только объекты PointTrack
                else:
                    raise TypeError(
                        "Все элементы должны быть объектами PointTrack или координатами (числами)"
                    )

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        if isinstance(pt, PointTrack):
            self.__points.append(pt)

    def add_front(self, pt):
        if isinstance(pt, PointTrack):
            self.__points.insert(0, pt)

    def pop_back(self):
        last_element = self.__points[-1]
        self.__points.remove(last_element)

    def pop_front(self):
        first_element = self.__points[0]
        self.__points.remove(first_element)


class PointTrack:

    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("координаты должны быть числами")
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("координаты должны быть числами")
        super().__setattr__(key, value)

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"
