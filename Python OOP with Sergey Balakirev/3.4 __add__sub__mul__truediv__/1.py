class NewList:

    def __init__(self, lst=None):
        if lst is None:
            self.lst = []
        else:
            self.lst = lst[:]

    @staticmethod
    def list_sub_list(a, b):
        b_copy = [(x, type(x)) for x in b]  # Создаем копию списка b
        result = []
        for x in a:
            if (x, type(x)) not in b_copy:
                result.append(x)
            else:
                b_copy.remove(
                    (x, type(x))
                )  # Удаляем только из копии b, чтобы не было проблем
        return result

    def __sub__(self, other):
        other_lst = other if not isinstance(other, NewList) else other.lst
        s = self.list_sub_list(self.lst, other_lst)
        return NewList(s)

    def __rsub__(self, other):
        s = self.list_sub_list(other, self.lst)
        return NewList(s)

    def get_list(self):
        return self.lst
