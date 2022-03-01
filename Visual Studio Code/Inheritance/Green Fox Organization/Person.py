class Person():

    def __init__(self, name: str = 'Jane Doe', age: int = 30, gender: str = 'female'):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print('Hi, I am ' + self.name + ' a ' +
              str(self.age) + ' year old ' + self.gender)
        print()

    def get_goal(self):
        print('My goal is: Live for the moment!')
