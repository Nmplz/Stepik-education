# здесь объявляйте класс
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        return super(TupleLimit, cls).__new__(cls, tuple(lst))

    def __init__(self, lst, max_length):
        self.max_length = max_length
        self.lst = lst
        self.max_len_check(self.lst)

    def max_len_check(self, obj):
        if not len(obj) <= self.max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __str__(self):
        return ' '.join(str(x) for x in self.lst)


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    t = TupleLimit(digits, 5)
    print(t)
except ValueError:
    print('число элементов коллекции превышает заданный предел')

