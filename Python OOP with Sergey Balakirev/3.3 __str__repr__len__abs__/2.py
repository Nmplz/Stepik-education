class Model:
    def __init__(self):
        self.args = None

    def query(self, **kwargs):
        self.args = kwargs  # {'args': {'id': 1, 'fio': 'Sergey', 'old': 33}}

    def __str__(self):
        if self.args is None:
            return "Model"
        else:
            res = "Model:"
            for x in self.args:
                res += f" {x} = {self.args[x]},"
            return res[:-1]
