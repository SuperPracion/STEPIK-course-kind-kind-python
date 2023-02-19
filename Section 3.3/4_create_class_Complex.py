from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.value_validator(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.value_validator(value)
        self.__img = value

    @classmethod
    def value_validator(cls, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.__real*self.__real + self.__img*self.__img)

cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)