from Person import Person
from BPSAttendee import BPSAttendee
from BPSMentor import BPSMentor


person = Person('Tamás', 21, 'male')

person.introduce()

person2 = BPSAttendee('Gábor', 33, 'male', 6098730, 'teacher')

person2.introduce()

person3 = BPSMentor('Adalbertína', 234, 'female', 676799,
                    'cleaning lady', ['biology', 'fisics'])

person3.introduce()
