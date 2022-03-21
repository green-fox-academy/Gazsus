
class Plant():

    def __init__(self, color: str, water_level: int, absorb_level: int,  needs_water_at: int, ):
        self.color = color
        self.water_level = water_level
        self.absorb_level = absorb_level
        self.needs_water_at = needs_water_at

    def water_plant(self, amount):
        if self.water_level < self.needs_water_at:
            self.water_level += amount*self.absorb_level
