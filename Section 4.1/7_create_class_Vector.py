class Vector:
    def __init__(self, *args):
        self.nums = args

    def __len__(self):
        return len(self.nums)

    def __size_validator(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__size_validator(other)
        res = [nums[0] + nums[1] for nums in zip(self.nums, other.nums)]

        if type(self) == VectorInt and type(other) == VectorInt:
            return VectorInt(*res)
        else:
            return Vector(*res)

    def __sub__(self, other):
        self.__size_validator(other)
        return Vector(*[nums[0] - nums[1] for nums in zip(self.nums, other.nums)])

    def get_coords(self):
        return self.nums

class VectorInt(Vector):
    def __init__(self, *args):
        self.__int_validator(args)
        super().__init__(*args)

    def __int_validator(self, values):
        if not all([isinstance(x, int) for x in values]):
            raise ValueError('координаты должны быть целыми числами')


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
#
v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
#
try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"
#
v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"