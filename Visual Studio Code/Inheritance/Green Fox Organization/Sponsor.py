from Person import Person


class Sponsor(Person):

    def __init__(self, name: str = 'Jane Doe', age: int = 30, gender: str = 'female', company: str = 'Google', hired_students: int = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print("Hi, I'm " + self.name + " , a " + str(self.age) + " year old " + self.gender +
              " who represents " + self.company + " and hired " + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1

    def get_goal(self):
        print('Hire brilliant junior software developers')
