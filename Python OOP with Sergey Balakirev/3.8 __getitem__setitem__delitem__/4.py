class TableValues:
    def __init__(self, rows, cols, cell=None):
        self.rows = rows
        self.cols = cols
        self.cell = cell
        self.cells = tuple(
            tuple(self.cell() for col in range(cols)) for row in range(rows)
        )

    def __setattr__(self, key, value):
        if key == "cell" and not value:
            raise ValueError("параметр cell не указан")
        super().__setattr__(key, value)

    def __getitem__(self, item):
        key_a, key_b = item
        return self.cells[key_a][key_b].value

    def __setitem__(self, key, value):
        key_a, key_b = key
        self.cells[key_a][key_b].value = value


class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("возможны только целочисленные значения")
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value
