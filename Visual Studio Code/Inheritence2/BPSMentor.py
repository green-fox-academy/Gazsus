from BPSAttendee import BPSAttendee


class BPSMentor(BPSAttendee):

    def __init__(self, name: str, age: int, gender: str, card_id: int, position: str, classes):
        super().__init__(name, age, gender, card_id, position)
        self.classes = classes

    def introduce(self):
        super().introduce()
        print(' I am also assigned to classes ' + str(self.classes) + '.')
        print()
