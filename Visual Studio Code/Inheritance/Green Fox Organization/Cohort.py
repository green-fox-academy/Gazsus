
from Student import Student
from Mentor import Mentor


class Cohort():

    def __init__(self, name):
        self.name = name
        self.students = []
        self.mentors = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_mentor(self, mentor: Mentor):
        self.mentors.append(mentor)

    def info(self):
        print("The " + self.name + " cohort has " + str(len(self.students)) +
              " students and " + str(len(self.mentors)) + " mentors.")
