class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, "rus-word", False))
