# - Create an array variable named `numbers` with the following content:
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

numbers = [3, 4, 5, 6, 7]


def double(list):
    return [i*2 for i in numbers]


print(double(numbers))
