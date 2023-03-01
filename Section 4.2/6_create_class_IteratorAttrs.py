class IteratorAttrs:
    def __iter__(self):
        for obj in self.__dict__.items():
            yield obj


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone(123, 12, 32)

for attr, value in phone:
    print(attr, value)
