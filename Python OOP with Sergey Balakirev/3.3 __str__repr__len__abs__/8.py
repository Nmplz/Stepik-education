class Recipe:
    def __init__(self, *args):
        self.recipe = []

        for i in args:
            self.recipe.append(i)

    def __len__(self):
        return len(self.recipe)

    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        for i in self.recipe:
            if i == ing:
                self.recipe.remove(i)

    def get_ingredients(self):
        return tuple(self.recipe)


class Ingredient:

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"
