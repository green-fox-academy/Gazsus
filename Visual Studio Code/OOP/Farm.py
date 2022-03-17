
from Animal import Animal


class Farm():

    def __init__(self):
        self.list_of_animals = []
        self.animal_limit = 40

    def breed(self):
        if len(self.list_of_animals) < self.animal_limit:
            self.list_of_animals.append(Animal())

    def sell(self):
        if len(self.list_of_animals) > 0:
            sellable_animal = self.list_of_animals[0]
            for animal in self.list_of_animals:
                if sellable_animal.hunger >= animal.hunger:
                    sellable_animal = animal
            self.list_of_animals.remove(sellable_animal)

    def __str__(self):
        animals = ""
        for animal in self.list_of_animals:
            animals += str(animal) + "\n"
        return animals


animal = Animal(12, 54)
