class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def _check_value(self, value):
        if not self._min_value < value < self._max_value:
            raise CellIntegerException("значение выходит за допустимый диапазон")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._check_value(value)
        self._value = value


class CellInteger(Cell):

    def _check_value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException("значение выходит за допустимый диапазон")


class CellFloat(Cell):
    def _check_value(self, value):
        if not self._min_value < value < self._max_value:
            raise CellFloatException("значение выходит за допустимый диапазон")


class CellString(Cell):
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    def _check_value(self, value):
        if not self._min_length < len(value) < self._max_length:
            raise CellStringException("длина строки выходит за допустимый диапазон")


class TupleData:
    def __init__(self, *args):
        self.tuple = list(args)

    def __len__(self):
        return len(self.tuple)

    def _indx_check(self, indx):
        if not type(indx) is int or not 0 <= indx < len(self):
            raise IndexError

    def __getitem__(self, indx):
        self._indx_check(indx)
        return self.tuple[indx].value

    def __setitem__(self, indx, value_):
        self._indx_check(indx)
        self.tuple[indx].value = value_

    def __iter__(self):
        for cel in self.tuple:
            yield cel.value


# эти строчки в программе не менять!
ld = TupleData(
    CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100)
)

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
