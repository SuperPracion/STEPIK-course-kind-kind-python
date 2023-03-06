class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

class Money:
    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = self.__int_or_float_validator(value)

    @staticmethod
    def __int_or_float_validator(value):
        if not type(value) in (int, float):
            raise TypeError('сумма должна быть числом')
        return value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"