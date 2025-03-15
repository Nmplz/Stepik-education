class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.ar = [self.cell() for _ in range(self.max_length)]

    def __len__(self):
        return len(self.max_length)

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item < self.max_length:
            return self.ar[item].value
        raise IndexError("неверный индекс для доступа к элементам массива")

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < self.max_length:
            self.ar[key].value = value
        else:
            raise IndexError("неверный индекс для доступа к элементам массива")

    def __str__(self):
        return " ".join([str(x.value) for x in self.ar])


class Integer:
    def __init__(self, start_value=0):
        self.value = start_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError("должно быть целое число")
        self._value = value
