from Person import Person


class Student(Person):

    def __init__(self, name: str = 'Jane Doe', age: int = 30, gender: str = 'female', previous_organization: str = 'The School Life', skipped_days: int = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print('Be a junior software developer')

    def introduce(self):
        print("Hi, I'm " + self.name + " , a " + str(self.age) + " year old " + self.gender + " from " +
              self.previous_organization + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
