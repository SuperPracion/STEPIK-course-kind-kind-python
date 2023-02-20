class Stack:
    def __init__(self):
        self.top = None
        self.lst_math = []

    def push_back(self, obj):
        if self.lst_math:
            self.lst_math[-1].next = obj

        self.lst_math.append(obj)

        if self.top is None:
            self.top = obj

    def pop_back(self):
        try:
            self.lst_math.remove(-1)
            self.lst_math[-1].next = None
        except:
            pass

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for data in other:
            self.push_back(StackObj(data))
        return self

    def __imul__(self, other):
        self.__mul__(other)
        return self

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
