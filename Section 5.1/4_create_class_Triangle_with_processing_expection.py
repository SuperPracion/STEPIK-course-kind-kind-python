class Triangle:
    def __init__(self, a, b, c, *args):
        self._a = self.__value_validator(a)
        self._b = self.__value_validator(b)
        self._c = self.__value_validator(c)

        self.__triagle_validator(self._a, self._b, self._c)

    @staticmethod
    def __value_validator(x):
        if type(x) not in (float, int) or x <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return float(x)

    @staticmethod
    def __triagle_validator(a, b, c):
        if (a > b + c) or (b > a + c) or (c > a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []

for params in input_data:
    try:
        lst_tr.append(Triangle(*params))
    except:
        pass
