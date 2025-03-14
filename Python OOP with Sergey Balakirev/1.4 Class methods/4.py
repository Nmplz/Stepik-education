import sys

lst_in = list(
    map(str.strip, sys.stdin.readlines())
)  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    # здесь добавлять методы
    def insert(self, data):
        lst = [{self.FIELDS[i]: key for i, key in enumerate(x.split())} for x in data]
        for i in lst:
            self.lst_data.append(i)

    def select(self, a, b):
        return self.lst_data[a : b + 1]


db = DataBase()
db.insert(lst_in)
