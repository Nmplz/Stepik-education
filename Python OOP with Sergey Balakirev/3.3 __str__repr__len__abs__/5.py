from math import sqrt


class Complex:
    def __init__(self, real, img):
        self._real = real
        self._img = img

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        if not isinstance(real, (int, float)):
            raise ValueError("Неверный тип данных.")
        self._real = real

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        if not isinstance(img, (int, float)):
            raise ValueError("Неверный тип данных.")
        self._img = img


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
