class Tuple(tuple):
    def __add__(self, other):
        print(other)
        return Tuple(super().__add__(tuple(other)))


t = Tuple([1, 2, 3])
t = t + "Python"
t = (t + "Python") + "ООП"
print(t)
