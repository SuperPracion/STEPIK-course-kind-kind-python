class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        try:
            return self.__dict__[tuple(self.__dict__)[item]]
        except:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        try:
            self.__dict__[tuple(self.__dict__)[key]] = value
        except:
            raise IndexError('неверный индекс')

    def __iter__(self):
        return iter(self.__dict__.values())
