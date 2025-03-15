class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.stack_len = 0
        self._iter = self.top

    def __iter__(self):
        self._iter = self.top
        yield self._iter.next

    # def __next__(self):
    #     self._iter = self._iter.next
    #     return self._iter

    def __len__(self):

        return self.stack_len

    def __getitem__(self, item):

        if not isinstance(item, int) or not (0 <= item < len(self)):
            raise IndexError("неверный индекс")

        counter = 0
        h = self.top
        while counter < item:
            h = h.next
            counter += 1
        return h.data

    def __setitem__(self, key, value):

        if not isinstance(key, int) or not (0 <= key < len(self)):
            raise IndexError("неверный индекс")

        counter = 0
        h = self.top
        while counter < key:
            h = h.next
            counter += 1
        h.data = value

    def push_back(self, obj):

        if self.tail:
            self.tail.next = obj
        if not self.top:
            self.top = obj
        self.tail = obj
        self.stack_len += 1

    def push_front(self, obj):

        obj.next = self.top
        self.top = obj
        self.stack_len += 1

    def pop(self):

        if self.top is None:
            return None  # Стек пуст

        if self.top == self.tail:  # Один элемент в стеке
            obj = self.top
            self.top = self.tail = None
        else:
            h = self.top
            while h.next != self.tail:
                h = h.next
            obj = self.tail
            self.tail = h
            self.tail.next = None

        self.stack_len -= 1
        return obj
