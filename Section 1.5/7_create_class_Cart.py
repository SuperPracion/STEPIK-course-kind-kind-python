class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, goods=list()):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, index):
        del self.goods[index]

    def get_list(self):
        return [f'{good.name}:{good.price}' for good in self.goods]


cart = Cart()
cart.add(TV('1', 1))
cart.add(TV('2', 2))
cart.add(Table('3', 3))
cart.add(Notebook('4', 4))
cart.add(Notebook('5', 5))
cart.add(Cup('6', 6))

print(cart.get_list())