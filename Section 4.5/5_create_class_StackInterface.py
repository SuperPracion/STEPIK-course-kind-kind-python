from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._count_objs  = 0

    def push_back(self, obj):
        last = self[self._count_objs - 1] if self._count_objs > 0 else None

        if last:
            last._next = obj

        if self._top is None:
            self._top = obj

        self._count_objs += 1

    def pop_back(self):
        if self._count_objs == 0:
            return None

        last = self[self._count_objs - 1]

        if self._count_objs == 1:
            self._top = None
        else:
            self[self._count_objs - 2]._next = None

        self._count_objs -= 1
        return last

    def __check_index(self, item):
        if not isinstance(item, int) or not (0 <= item < self._count_objs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self._top
        while h and count < item:
            h = h._next
            count += 1

        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value._next = obj._next

        if prev._next:
            prev._next = value


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"
#
#
st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"
#
obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"
#
obj = StackObj("obj")
st.push_back(obj)
#
n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1
#
assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"