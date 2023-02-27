class SparseTable:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.db = {}

    def update_row_and_cols(self):
        self.rows = max(self.db, key=lambda x: x[0])[0] + 1
        self.cols = max(self.db, key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        self.db[(row, col)] = data
        self.update_row_and_cols()

    def remove_data(self, row, col):
        try:
            del self.db[(row, col)]
            self.update_row_and_cols()
        except:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        try:
            return self.db[item[0], item[1]].value
        except:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        self.add_data(key[0], key[1], Cell(value))


class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

print(st.db)

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"

