class Digit:
    def __init__(self, value):
        if type(value) == str:
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')



class Float(Digit):
    def __init__(self, value):
        super().__init__(value)

        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)

        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)

        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5), FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = [*filter(lambda x: x.value >= 0, digits)]
lst_float = [*filter(lambda x: type(x.value) == float, digits)]