# def devision(divident, divisor):
#    try:
#       return divident / divisor
#    except ZeroDivisionError:
#       print("Couldn't divide number")
#   except ArithmeticError:
#       print("Unexpected error")
#    finally:
#        print(" a ")


#(devision(10, 0))


# -----------------------------------------------------
# Write a function that receives a file name
# and reads the contents of that file
# It prints the contents to the console line by line
# In case of any errors: print('Error: something went wrong with ' + file_name)

from termcolor import cprint


def readFile(file_name):
    try:
        file = open(file_name, 'r')
        content = file.readlines()
        for line in content:
            print(line)
    except:
        cprint('Unexpected error: something went wrong with ' +
               file_name, color='red')


readFile('C:\Users\GAZSI\Sulis Piton\Gazsus\FileManipulation\List.txt')
