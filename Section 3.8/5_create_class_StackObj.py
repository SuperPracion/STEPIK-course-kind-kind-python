class Stack:
    def __init__(self):
        self.top = None
        self.__count_objs  = 0

    def push(self, obj):
        last = self[self.__count_objs - 1] if self.__count_objs > 0 else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

        self.__count_objs += 1

    def pop(self):
        if self.__count_objs == 0:
            return None

        last = self[self.__count_objs - 1]

        if self.__count_objs == 1:
            self.top = None
        else:
            self[self.__count_objs - 2].next = None

        self.__count_objs -= 1
        return last

    def __check_index(self, item):
        if not isinstance(item, int) or not (0 <= item < self.__count_objs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1

        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next

        if prev.next:
            prev.next = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

