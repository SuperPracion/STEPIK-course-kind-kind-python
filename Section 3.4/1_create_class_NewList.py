class NewList:
    def __init__(self, value=[]):
        self.list_value = value

    def __sub__(self, other):
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self.list_value, other_list))

    def __rsub__(self, other):
        return NewList(self.__diff_list(other, self.list_value))

    def get_list(self):
        return self.list_value

    @staticmethod
    def __diff_list(list_value, other_list):
        if len(other_list) == 0:
            return list_value

        sub = other_list[:]
        return [x for x in list_value if not NewList.__is_element(x, sub)]

    @staticmethod
    def __is_element(x, sub):
        res = any(map(lambda xx: type(xx) == type(x) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list())
