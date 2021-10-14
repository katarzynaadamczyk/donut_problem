class Donut:

    def __init__(self, weight, kcal, name):
        self.weight = weight
        self.kcal = kcal
        self.name = name
        self.kcalper1g = kcal / weight

    def print_donut(self):
        print(f'{self.name}: {self.weight} g, {self.kcal} kcal')