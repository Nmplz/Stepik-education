from abc import ABC, abstractmethod


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_obj):
        self._next = next_obj

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):

    def __init__(self):
        self._top = None
        self._last = None

    def push_back(self, obj):
        if self._last:
            self._last.next = obj
        if not self._top:
            self._top = obj
        if not self._last:
            self._last = obj
        self._last = obj

    def pop_back(self):
        if self._top is None:
            return None  # Если стек пустой, возвращаем None

        if self._top == self._last:  # Если в стеке один элемент
            last_obj = self._last
            self._top = self._last = None
            return last_obj

        h = self._top
        while h.next != self._last:
            h = h.next

        last_obj = self._last
        self._last = h
        self._last.next = None
        return last_obj

    def __add__(self, other):
        if isinstance(other, StackObj):
            self._last.next = other
            self._last = other
        return self

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        for i in other:
            self + StackObj(i)
        return self
