class BPSAttendee():

    def __init__(self, name: str, age: int, gender: str, card_id: int, position: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.card_id = card_id
        self.position = position

    def introduce(self):
        print('Hi, my name is ' + self.name + '. I am ' +
              str(self.age) + ' years old and I am ' + self.gender + '.')
        print('My card id is ' + str(self.card_id) +
              ' and my position is, ' + self.position + '.')
        print()
