# здесь объявите класс TriangleChecker


a, b, c = map(int, input().split())  # эту строчку не менять


# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ok_type(self):
        if (
            (type(self.a) in (int, float))
            and (type(self.b) in (int, float))
            and (type(self.c) in (int, float))
        ):
            if self.a > 0 and self.b > 0 and self.c > 0:
                return True
            return False
        return False

    def ok_dlinna(self):
        return (
            self.a + self.b > self.c
            and self.a + self.c > self.b
            and self.b + self.c > self.a
        )

        return False

    def is_triangle(self):
        if not self.ok_type():
            return 1
        if not self.ok_dlinna():
            return 2
        else:
            return 3


#
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
