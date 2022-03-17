class Animal:
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

    def __str__(self):
        return "hunger: " + str(self.hunger) + " thirst: " + str(self.thirst)


class Farm:
    def __init__(self):
        self.list_of_animals = []
        self.animal_limit = 10

    def breed(self):
        if len(self.list_of_animals) < self.animal_limit:
            self.list_of_animals.append(Animal())

    def sell(self):
        if len(self.list_of_animals) > 0:
            fullest = self.list_of_animals[0]
            for animal in self.list_of_animals:
                if fullest.hunger >= animal.hunger:
                    fullest = animal
            self.list_of_animals.remove(fullest)

    def __str__(self):
        animals = ""
        for animal in self.list_of_animals:
            animals += str(animal) + "\n"
        return animals


farm = Farm()
for i in range(3):
    farm.breed()
print(farm)
farm.list_of_animals[0].play()
farm.list_of_animals[0].drink()
farm.list_of_animals[1].play()
farm.list_of_animals[1].play()
print(farm)
farm.sell()
print(farm)
