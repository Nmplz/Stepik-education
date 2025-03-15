class ListInteger(list):
    @staticmethod
    def _int_check(value):
        if type(value) != int:
            raise TypeError("можно передавать только целочисленные значения")
        return True

    def __init__(self, lst):
        if all(self._int_check(x) for x in lst):
            super().__init__(lst)

    def __setitem__(self, key, value):
        self._int_check(value)
        super().__setitem__(key, value)

    def append(self, __object):
        self._int_check(__object)
        super().append(__object)
