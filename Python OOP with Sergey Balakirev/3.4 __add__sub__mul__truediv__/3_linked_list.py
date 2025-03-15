class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:

    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.last:
            self.last.next = obj
        if not self.top:
            self.top = obj
        if not self.last:
            self.last = obj
        self.last = obj

    def pop_back(self):
        h = self.top
        while h:
            if h.next == self.last:
                self.last = h
                h.next = None
            h = h.next

    def __add__(self, other):
        if isinstance(other, StackObj):
            self.last.next = other
            self.last = other
        return self

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        for i in other:
            self + StackObj(i)
        return self
