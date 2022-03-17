
from Person import Person
from enum import Enum


class Level(Enum):
    junior = 1
    intermediate = 2
    senior = 3


class Mentor(Person):

    def __init__(self, name: str = 'Jane Doe', age: int = 30, gender: str = 'female', level: Level = Level.intermediate):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print('Educate brilliant junior software developers')

    def introduce(self):
        print("Hi, I'm " + self.name + " , a " + str(self.age) +
              " year old gender " + str(self.level) + " mentor.")
