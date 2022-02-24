from monster import Monster
from human import Human


monster1 = Monster('Kázmér', 'male', 32)
monster2 = Monster('Brünhilda', 'female', 19081)
monster3 = Monster('Esztebán', 'male', 47)

monster2.eat_human(Human("Human 1"))

monster1.introduce()
monster2.introduce()
monster3.introduce()