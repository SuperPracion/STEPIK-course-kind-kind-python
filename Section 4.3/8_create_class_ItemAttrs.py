class ItemAttrs:
    def __init__(self, *args):
        self.nums = list(*args)

    def __getitem__(self, index):
        try:
            return self.nums[index]
        except:
            pass

    def __setitem__(self, key, value):
        try:
            self.nums[key] = value
        except:
            pass


class Point(ItemAttrs):
    def __init__(self, *args):
        super().__init__(args)


pt = Point(1, 2.5)
print(pt.nums)
x = pt[0]  # 1
print(x)
y = pt[1]  # 2.5
print(y)
pt[0] = 10
print(pt[0])
