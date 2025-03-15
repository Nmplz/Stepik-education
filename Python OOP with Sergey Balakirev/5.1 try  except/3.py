# считывание строки и разбиение ее по пробелам
lst_in = input().split()


def int_checker(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(int_checker, lst_in))
