import sys

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))


lst_in = list(map(str.strip, sys.stdin.readlines()))


lst_bs = [BookStudy(*obj.split(';')) for obj in lst_in]
unique_books = len(set(hash(book) for book in lst_bs))
