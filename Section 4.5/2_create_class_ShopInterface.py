class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    unique_id = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = self.__get_unique_id()

    def get_id(self):
        return self._id

    @classmethod
    def __get_unique_id(cls):
        ShopItem.unique_id += 1
        return cls.unique_id
