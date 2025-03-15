import sys

# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))


class Player:

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)

    def __repr__(self):
        return f"{self.name}: {self.score}"


players = []
for x in lst_in:
    a, b, c = x.split(";")
    players.append(Player(a, b, int(c)))

players_filtered = list(filter(bool, players))
