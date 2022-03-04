
from Car import Car


class Station():

    def __init__(self):
        self.gas_amount = 99999999

    def refill(self):
        self.gas_amount -= Car.capacity
        Car.gas_amount = Car.capacity
