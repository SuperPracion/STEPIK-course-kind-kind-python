class Cell:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def __value_validator(self, value):
        r, c = value

        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__value_validator(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__value_validator(key)

        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

        self.cells[key[0]][key[1]].value = value

    def __iter__(self):
        for row in self.cells:
            yield (x.data for x in row)


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

