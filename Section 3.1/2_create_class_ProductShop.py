class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    product_counter = 0

    def __init__(self, name='', weight=0, price=0):
        self.id = self.id_gen()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in ('weight', 'price', 'id') and type(value) in (int, float) and value >= 0:
            object.__setattr__(self, key, value)
        elif key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

        object.__delattr__(self, item)

    @classmethod
    def id_gen(cls):
        cls.product_counter += 1
        return cls.product_counter


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
