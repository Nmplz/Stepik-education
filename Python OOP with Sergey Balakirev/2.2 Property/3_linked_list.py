class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__priv = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next == None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def priv(self):
        return self.__priv

    @priv.setter
    def priv(self, priv):
        self.__priv = priv


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        obj.priv = self.last
        self.last = obj
        if not self.top:
            self.top = obj

    def pop(self):
        if self.last is None:
            return
        poped = self.last
        prev = self.last.priv
        if prev:
            prev.next = None
        self.last = prev
        if self.last is None:
            self.top = None
        return poped

    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s
