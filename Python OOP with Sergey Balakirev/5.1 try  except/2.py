# считывание строки и разбиение ее по пробелам
lst_in = input().split()


def int_checker(value):
    try:
        return int(value)
    except:
        return False


lst_sum = sum([int(x) for x in lst_in if int_checker(x)])
print(lst_sum)
