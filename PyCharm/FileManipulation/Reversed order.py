def decrypt(file_name):
    file = open('output2.txt', 'w')

    with open(file_name, 'r') as myfile:
        data = myfile.readlines()

    data_2 = data[::-1]

    file.writelines(data_2)

    file.close()

decrypt('reversed_order.txt')