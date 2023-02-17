import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if self.slots[slot_num] is None:
            if isinstance(filter, Mechanical) and slot_num == 1:
                self.slots[1] = filter
            elif isinstance(filter, Aragon) and slot_num == 2:
                self.slots[2] = filter
            elif isinstance(filter, Calcium) and slot_num == 3:
                self.slots[3] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num] = None

    def get_filters(self):
        return self.slots.values()

    def water_on(self):
        return None not in self.slots.values() and all(
            [0 <= time.time() - filter.date <= self.MAX_DATE_FILTER for filter in self.slots.values()])


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)

