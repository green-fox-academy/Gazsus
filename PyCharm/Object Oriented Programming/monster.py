from human import Human

class Monster:

    def __init__(self, name: str, gender: str, age: int = 0):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__thirst = 0
        self.__hunger = 0
        self.__humans_eaten = []

    # Setter

    def set_age(self, age: int):
        if age > 0:
            self.__age = age

    # Getter

    def get_age(self) -> int:
        return self.__age

    # Eat human

    def eat_human(self, human: Human):
        self.__humans_eaten.append(human)
        human.kill()

    def get_eaten_humans(self) -> []:
        return self.__humans_eaten

    # Drink water

    def drink_water(self):
        self.__thirst -= 5

    # Run

    def run(self):
        self.__hunger += 3
        self.__thirst += 6

    # Introduce

    def introduce(self):
        human_string = ''
        for human in self.__humans_eaten:
            human_string += str(human) + ', '
        print('Hi, my name is ' + self.__name + ', my age is ' + str(self.__age) + ' and I have eaten ' + str(
            human_string))

    # String representer

    def __str__(self) -> str:
        return self.__name