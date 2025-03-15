class Record:
    def __init__(self, **kwargs):
        for field_name, value in kwargs.items():
            self.__dict__.setdefault(field_name, value)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, item):
        if item < len(self):
            _item = list(self.__dict__)[item]
            return self.__dict__[_item]
        raise IndexError("неверный индекс поля")

    def __setitem__(self, key, value):
        _key = list(self.__dict__)[key]
        self.__dict__[_key] = value


def __delitem__(self, key):
    _key = list(self.__dict__)[key]
    del self.__dict__[_key]
