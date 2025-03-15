import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = []


for i in lst_in:
    name, author, year = i.split(";")
    lst_bs.append(BookStudy(name, author, year))

unique_books = len(set(lst_bs))
