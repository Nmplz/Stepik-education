class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if self.head is None:
            self.head = obj

    def __len__(self):
        h = self.head
        len_counter = 0

        while h:
            len_counter += 1
            h = h.next
        return len_counter

    def __call__(self, indx):
        obj = self.__get_obj__by_index(indx)
        return obj.data if obj else None

    def __get_obj__by_index(self, indx):
        h = self.head
        indx_counter = 0

        while h and indx_counter < indx:
            indx_counter += 1
            h = h.next
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj__by_index(indx)
        if obj is None:
            return
        prev_obj = obj.prev
        next_obj = obj.next
        if prev_obj:
            prev_obj.next = next_obj
        if next_obj:
            next_obj.prev = prev_obj

        if self.head == obj:
            self.head = next_obj
        if self.tail == obj:
            self.tail = prev_obj


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev
