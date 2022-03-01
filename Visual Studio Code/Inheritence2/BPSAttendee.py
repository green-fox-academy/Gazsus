from Person import Person


class BPSAttendee(Person):

    def __init__(self, name: str, age: int, gender: str, card_id: int, position: str):
        super().__init__(name, age, gender)
        self.card_id = card_id
        self.position = position

    def introduce(self):
        super().introduce()
        print('My card id is ' + str(self.card_id) +
              ' and my position is, ' + self.position + '.')
