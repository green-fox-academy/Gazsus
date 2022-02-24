# Write a function that is able to manipulate a file
# by writing your name into it as a single line.
# The file should be named "my-file.txt".
# In case the program is unable to write the file,
# it should print the following error message: "Unable to write file: my-file.txt"


def write_in_file(text):
    try:
        file = open('my-file.txt', 'a')
        file.write(text)
        file.close()
    except:
        print("Unable to write file: my-file.txt")


write_in_file('Gazsi')

