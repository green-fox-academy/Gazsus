
from numpy import var


List_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

List_B = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

if 'Durian' in List_A:
    print('true')
else:
    print('false')

List_B.remove(List_B[3])

var = "Kiwifruit"

List_A.insert(4, var)

a = set(List_A)
b = set(List_B)

if a == b:
    print("true")
else:
    print("fasle")

index_1 = List_A.index('Avocado')

print(index_1)

#index_2 = List_B.index('Durian')

# print(index_2)

# Can't print index, Durian is not on list

List_B.extend(['Passion Fruit', 'Pomelo'])

print(List_A)
print(List_B)
