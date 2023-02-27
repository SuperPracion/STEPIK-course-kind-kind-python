class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj

        self.__last = obj

    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __get_obj(self, indx):
        if type(indx) != int or not (0 <= indx < sum(1 for _ in self)):
            raise IndexError('неверный индекс')

        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, indx):
        return self.__get_obj(indx).data

    def __setitem__(self, key, value):
        self.__get_obj(key).data = value

    def __iter__(self):
        current = self.top

        while current:
            yield current
            current = current.next


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
