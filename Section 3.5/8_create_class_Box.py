class Box:
    def __init__(self):
        self.pool = []
        self.total_mass = 0

    def add_thing(self, obj):
        self.pool.append(obj)
        self.total_mass += obj.mass

    def get_things(self):
        return self.pool

    def __eq__(self, other):
        return self.total_mass == other.total_mass and all([other.pool.count(obj) == 1 for obj in self.pool])


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
