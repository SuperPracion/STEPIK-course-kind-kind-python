import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return DataBase.lst_data[a: min(b+1, len(DataBase.lst_data))]

    def insert(self, data):
        for person in data:
            DataBase.lst_data += dict(zip(DataBase.FIELDS, person.split()))

db = DataBase()
db.insert(lst_in)
