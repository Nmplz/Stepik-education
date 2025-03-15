class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int) and other < len(self):
            for i, v in enumerate(self.book_list):
                if i == other:
                    self.book_list.remove(self.book_list[i])
        return self


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
