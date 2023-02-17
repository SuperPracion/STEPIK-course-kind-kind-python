class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        allowed_keys = {
            'title': str,
            'author': str,
            'pages': int,
            'year': int
        }
        if key in allowed_keys and type(value) == allowed_keys[key]:
            self.__dict__[key] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
