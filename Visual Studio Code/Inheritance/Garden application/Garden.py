from Plant import Plant
from Flower import Flower
from Tree import Tree


class Garden():

    def __init__(self):
        self.plants = []

    def water_all_plants(self, amount):
        thirsty_plants = 0
        for plant in self.plants:
            if plant.water_level < plant.needs_water_at:
                thirsty_plants += 1
        for plant in self.plants:
            if plant.water_level < plant.needs_water_at:
                plant.water_plant(amount/thirsty_plants)
        print('Watering with ' + str(amount))

    def add_plant(self, plant):
        self.plants.append(plant)

    def show_status(self):
        for plant in self.plants:
            plant.print_status()
