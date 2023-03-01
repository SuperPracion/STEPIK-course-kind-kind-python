class ListInteger(list):
    def __init__(self, *args):
        super().__init__(self.__value_validator(x) for x in list(*args))

    def __setitem__(self, key, value):
        super().__setitem__(key, self.__value_validator(value))

    def append(self, value):
        super().append(self.__value_validator(value))

    @classmethod
    def __value_validator(cls, value):
        if type(value) == int:
            return value
        else:
            raise TypeError('можно передавать только целочисленные значения')

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)