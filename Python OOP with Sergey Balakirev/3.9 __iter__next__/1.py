class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

        self._attr = tuple(self.__dict__)
        self._len_attr = len(self._attr)
        self._iter_index = -1

    def __getitem__(self, index):
        if type(index) != int or not (-self._len_attr <= index <= self._len_attr):
            raise IndexError("неверный индекс")
        return getattr(self, self._attr[index])

    def __setitem__(self, key, value):
        if type(key) != int or not (-self._len_attr <= key <= self._len_attr):
            raise IndexError("неверный индекс")
        setattr(self, self._attr[key], value)

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < self._len_attr - 1:
            self._iter_index += 1
            return getattr(self, self._attr[self._iter_index])
        raise StopIteration
