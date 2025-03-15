class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    @classmethod
    def coord_check(cls, x):
        if isinstance(x, (int, float)) and cls.MIN_COORD < x < cls.MAX_COORD:
            return True
        return False

    def __init__(self, x=0, y=0):
        if self.coord_check(x) and self.coord_check(y):
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.coord_check(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.coord_check(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.__x * vector.__x + vector.__y * vector.__y