
from Plant import Plant


class Flower(Plant):

    def __init__(self, color: str):
        super().__init__(color, 1, 0.75, 5)

    def print_status(self):
        if self.water_level < self.needs_water_at:
            print('The ' + self.color + ' flower needs water')
        else:
            print("The " + self.color + " flower doesn't need water")
