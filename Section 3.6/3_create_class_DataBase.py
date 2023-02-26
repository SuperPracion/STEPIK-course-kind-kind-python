import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        res = tuple(filter(lambda x: x.pk == pk, (x for row in self.dict_db.values() for x in row)))
        return res[0] if len(res) > 0 else None


class Record:
    unique_id = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__get_unique_id()

    @classmethod
    def __get_unique_id(cls):
        cls.unique_id += 1
        return cls.unique_id

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('huita.db')

for obj in lst_in:
    args = list(map(str.strip, obj.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))
