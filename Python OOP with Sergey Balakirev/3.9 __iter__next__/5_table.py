class TableValues:
    def __init__(self, rows, cols, type_data=0):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = {}

    def __iter__(self):
        for x in range(self.rows):
            yield (
                self.cells.get((x, y), Cell(self.type_data)).data
                for y in range(self.cols)
            )

    def _cheking_index(self, indx):
        r, c = indx
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return True
        raise IndexError("неверный индекс")

    def __getitem__(self, item):
        self._cheking_index(item)
        return self.cells.get(item, Cell(self.type_data)).data

    def __setitem__(self, key, value):
        self._cheking_index(key)
        if type(self.type_data) != type(value):
            raise TypeError("неверный тип присваиваемых данных")
        self.cells[key] = Cell(value)


class Cell:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
