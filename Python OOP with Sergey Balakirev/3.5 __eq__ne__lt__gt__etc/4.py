class Morph:
    def __init__(self, *args):
        self.words = []
        for i, v in enumerate(args):
            setattr(self, f"word{i}", v.lower())
            self.words.append(v.lower())

    def __eq__(self, other):
        return other.lower() in self.words

    def __ne__(self, other):
        return other.lower() not in self.words

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)


dict_words = [
    Morph("связь", "связи", "связью", "связи", "связей", "связям", "связями", "связях"),
    Morph(
        "формула",
        "формулы",
        "формуле",
        "формулу",
        "формулой",
        "формул",
        "формулам",
        "формулами",
        "формулах",
    ),
    Morph(
        "вектор",
        "вектора",
        "вектору",
        "вектором",
        "векторе",
        "векторы",
        "векторов",
        "векторам",
        "векторами",
        "векторах",
    ),
    Morph(
        "эффект",
        "эффекта",
        "эффекту",
        "эффектом",
        "эффекте",
        "эффекты",
        "эффектов",
        "эффектам",
        "эффектами",
        "эффектах",
    ),
    Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях"),
]

text = input()
# text = 'Мы будем устанавливать связь завтра днем.'
lst_words = "".join([x.lower() for x in text if x not in "–?!,.;"])
counter = 0
for i in lst_words.split():
    if i in dict_words:
        counter += 1
print(counter)
