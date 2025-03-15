class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def __len__(self):
        return len(self.lst_words)


# ['Я к вам пишу  чего же боле', 'Что я могу еще сказать', 'Теперь я знаю в вашей воле', 'Меня презреньем наказать', 'Но вы к моей несчастной доле', 'Хоть каплю жалости храня', 'Вы не оставите меня']
stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня.",
]

lst_words = ["".join([char for char in x if char not in "–?!,.;"]) for x in stich]

lst_text = [StringText(lst.split()) for lst in lst_words]
lst_text_sorted = sorted(lst_text, key=len, reverse=True)
lst_text_sorted = [" ".join([y for y in x.lst_words]) for x in lst_text_sorted]
