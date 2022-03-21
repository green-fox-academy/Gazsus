from Tree import Tree
from Flower import Flower
from Plant import Plant
from Garden import Garden

pipacs = Flower('yellow')
kékvirág = Flower('blue')

narancsfa = Tree('orange')
lilafa = Tree('purple')

kert = Garden()

kert.add_plant(pipacs)
kert.add_plant(kékvirág)
kert.add_plant(narancsfa)
kert.add_plant(lilafa)

kert.show_status()
kert.water_all_plants(40)
kert.show_status()
kert.water_all_plants(70)
kert.show_status()
