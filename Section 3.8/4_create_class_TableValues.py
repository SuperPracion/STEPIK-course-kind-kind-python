class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        if not cell:
            raise ValueError('параметр cell не указан')

        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __value_validator(self, value):
        r, c = value
        if type(r) != int or type(c) != int or not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise ValueError('возможны только целочисленные значения')

    def __getitem__(self, item):
        self.__value_validator(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__value_validator(key)
        self.cells[key[0]][key[1]].value = value


tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"