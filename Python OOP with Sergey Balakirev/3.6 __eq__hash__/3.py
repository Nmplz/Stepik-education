import sys

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [record])

    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
                return i


class Record:
    _PK = 0

    def __new__(cls, *args, **kwargs):
        cls._PK += 1
        return super().__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self._PK

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('path')

for i in lst_in:
    fio, descr, old = i.split(';')
    key = Record(fio, descr, int(old))
    if key in db.dict_db:
        db.dict_db[key].append(key)
    else:
        db.write(key)