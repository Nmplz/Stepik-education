class Translator:
    def add(self, eng, rus):
        if "tr" not in self.__dict__:
            self.tr = {}

        if rus not in self.tr.setdefault(eng, []):
            self.tr.setdefault(eng, []).append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        return self.tr.get(eng, [])


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
print(*tr.translate("go"))
