
def read_file(file_name):
    try:
        file = open(file_name, 'r')
        content = file.readlines()
        for line in content:
            print(line)
    except IOError:
        print('Unexpected error: something went wrong with ' + file_name)


read_file('List.txt')
