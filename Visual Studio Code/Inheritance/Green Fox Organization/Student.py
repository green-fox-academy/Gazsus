from Person import Person


class Student(Person):

    def __init__(self, name: str = 'Jane Doe', age: int = 30, gender: str = 'female', previous_organizations: str = 'The School Life', skipped_days: int = 0):
        super().__init__(name, age, gender)
        self.previous_organizations = previous_organizations
        self.skipped_days = skipped_days
