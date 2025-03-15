s_inp = input()  # эту строку (переменную s_inp) в программе не менять


class Dimensions:
    def __init__(self, a, b, c):
        if not all(x > 0 for x in [a, b, c]):
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst = list(s_inp.split(";"))  # ['1 2 3', ' 4 5 6.78', ' 1 2 3', ' 3 1 2.5']
lst_dims = []
for i in lst:
    a, b, c = [int(x) if x.isdigit() else float(x) for x in i.split()]
    lst_dims.append(Dimensions(a, b, c))
lst_dims = sorted(lst_dims, key=hash)
