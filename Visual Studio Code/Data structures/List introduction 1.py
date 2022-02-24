
from os import remove
from turtle import clear


list = []
print(len(list))

list.append('Wiliam')

if len(list) == 0:
    print('true')
else:
    print('false')

list.append('John')
list.append('Amanda')

print(len(list))

print(list[2])

iter_len = len(list)
for i in range(iter_len):
    print(list[i])

for x, res in enumerate(list):
    print(x + 1, ":", res)

list.remove(list[1])

for i in reversed(list):
    print(i)

list.clear()

print(len(list))
