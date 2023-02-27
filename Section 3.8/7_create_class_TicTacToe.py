class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def clear(self):
        self.pole = TicTacToe().pole

    def __check_correct_index(self, key):
        try:
            return self.pole[key[0]][key[1]]
        except IndexError:
            raise IndexError('неверный индекс клетки')
        except ValueError:
            raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))

        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_correct_index(key)
        self.pole[key[0]][key[1]].value = value


class Cell:
    def __init__(self):
        self.is_free = False
        self.value = 0

    def __bool__(self):
        return self.is_free


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"

g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
#
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
