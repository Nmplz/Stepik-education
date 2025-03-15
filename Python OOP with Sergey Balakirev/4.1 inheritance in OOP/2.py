class Thing:
    ID = 0

    @classmethod
    def _get_id(cls):
        Thing.ID += 1
        return Thing.ID

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.id = self._get_id()
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (
            self.id,
            self.name,
            self.price,
            self.weight,
            self.dims,
            self.memory,
            self.frm,
        )


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
