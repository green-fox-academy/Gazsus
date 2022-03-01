class Person():

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print('Hi, my name is ' + self.name + '. I am ' +
              str(self.age) + ' years old and I am ' + self.gender)
        print()
