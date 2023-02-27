class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        try:
            return list(self.__dict__.values())[item]
        except:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        try:
            self.__dict__[list(self.__dict__.keys())[key]] = value
        except:
            raise IndexError('неверный индекс поля')


r = Record(pk=1, title='Python ООП', author='Балакирев')
r.pk  # 1
r.title  # Python ООП
r.author  # Балакирев
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[1])  # Супер курс по ООП
# r[3] # генерируется исключение IndexError
