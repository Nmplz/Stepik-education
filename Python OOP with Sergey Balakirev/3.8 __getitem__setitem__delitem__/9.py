class SparseTable:
    def __init__(self):

        self.cells = {}
        self.rows = 0
        self.cols = 0

    def __getitem__(self, item):
        try:
            return self.cells[item].value
        except:
            raise ValueError("данные по указанным индексам отсутствуют")

    def __setitem__(self, key, value):
        self.cells[key] = Cell(value)
        self.rows = max(self.cells, key=lambda x: x[0])[0] + 1
        self.cols = max(self.cells, key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        # добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
        self.cells[(row, col)] = data
        self.rows = max(self.cells, key=lambda x: x[0])[0] + 1
        self.cols = max(self.cells, key=lambda x: x[1])[1] + 1

    def remove_data(
        self, row, col
    ):  # удаление ячейки (объект класса Cell) с индексами (row, col).
        try:
            del self.cells[(row, col)]
            self.rows = max(self.cells, key=lambda x: x[0])[0] + 1
            self.cols = max(self.cells, key=lambda x: x[1])[1] + 1
        except:
            raise IndexError("ячейка с указанными индексами не существует")


class Cell:
    def __init__(self, value):
        self.value = value
