class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(len(self.lst)):
                if j == self.column:
                    yield self.lst[i][j]
