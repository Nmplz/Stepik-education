class Matrix:
    def __init__(self, *args):  # rows, cols, fill_value
        if len(args) == 1 and isinstance(args[0], list):
            if not (len(set([len(x) for x in args[0]])) == 1) or not all(
                type(x) == int for row in args[0] for x in row
            ):
                raise TypeError("список должен быть прямоугольным, состоящим из чисел")
            list2d = args[0]
            self.rows = len(list2d)
            self.cols = len(list2d[0])
            self.data = [row[:] for row in list2d]

        if len(args) == 3:
            rows, cols, fill_value = args
            self.rows = rows
            self.cols = cols
            self.fill_value = fill_value
            self.data = [
                [fill_value for cols in range(self.cols)] for row in range(self.rows)
            ]

    def __setattr__(self, key, value):
        if (
            key in ("rows", "cols")
            and isinstance(value, int)
            or key == "fill_value"
            and isinstance(value, (int, float))
        ):
            super().__setattr__(key, value)
        elif key == "data":
            super().__setattr__(key, value)
        else:
            raise TypeError(
                "аргументы rows, cols - целые числа; fill_value - произвольное число"
            )

    def __index_check(self, indx):
        if isinstance(indx, tuple) and not all(type(x) == int for x in indx):
            raise IndexError("недопустимые значения индексов")
        r, c = indx
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise IndexError("недопустимые значения индексов")

    @staticmethod
    def __value_check(value):
        if not isinstance(value, (int, float)):
            raise TypeError("значения матрицы должны быть числами")

    def __len_check(self, other):  ## проверка только для матриц
        if not len(self.data) == len(other.data):
            raise ValueError("операции возможны только с матрицами равных размеров")

    def __getitem__(self, item):
        self.__index_check(item)
        r, c = item
        return self.data[r][c]

    def __setitem__(self, key, value):
        self.__index_check(key)
        self.__value_check(value)
        r, c = key
        self.data[r][c] = value

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            self.__len_check(other)
            return Matrix(
                [
                    [self.data[x][y] + other.data[x][y] for y in range(self.cols)]
                    for x in range(self.rows)
                ]
            )
        return Matrix(
            [
                [self.data[x][y] + other for y in range(self.cols)]
                for x in range(self.rows)
            ]
        )

    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            self.__len_check(other)
            return Matrix(
                [
                    [self.data[x][y] - other.data[x][y] for y in range(self.cols)]
                    for x in range(self.rows)
                ]
            )
        return Matrix(
            [
                [self.data[x][y] - other for y in range(self.cols)]
                for x in range(self.rows)
            ]
        )
