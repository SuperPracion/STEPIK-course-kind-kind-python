import re
import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = {}

for info in lst_in:
    name, weight, price = re.search(r'^([^:]+):\s+([\d\.]+)\s+([\d\.]+)\s*$', info).groups()
    key = ShopItem(name, weight, price)
    if key in shop_items:
        shop_items[key][1] += 1
    else:
        shop_items[key] = [key, 1]
