class ListMath:
    def __init__(self, lst=None):
        if lst is None:
            self.lst_math = []
        else:
            self.lst_math = lst

    @property
    def lst_math(self):
        return self._lst_math

    @lst_math.setter
    def lst_math(self, lst):
        self._lst_math = [x for x in lst if type(x) in (int, float)]

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [x + other for x in self._lst_math]
            return ListMath(new_lst)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self + other

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [x - other for x in self._lst_math]
            return ListMath(new_lst)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [other - x for x in self._lst_math]
            return ListMath(new_lst)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [x * other for x in self._lst_math]
            return ListMath(new_lst)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [x / other for x in self._lst_math]
            return ListMath(new_lst)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            new_lst = [other / x for x in self._lst_math]
            return ListMath(new_lst)

    def __itruediv__(self, other):
        return self / other
