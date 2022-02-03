# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers`
# - Print the elements of the reversed `numbers`

numbers = [3, 4, 5, 6, 7]

for i in reversed(numbers):
    print(i)

# or

numbers.reverse()
print(numbers)
