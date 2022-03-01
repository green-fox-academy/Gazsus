
def decrypt(file_name):

    file = open('output.txt', 'w')

    with open(file_name, 'r') as myfile:
        data = myfile.read()


    data_2 = data[::-1]

    file.write(data_2)

    file.close()

decrypt('reversed_lines.txt')