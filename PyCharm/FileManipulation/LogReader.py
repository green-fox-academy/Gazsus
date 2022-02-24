# Read all data from 'log.txt'
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP addresses
# Write a function that returns the GET / POST request ratio

def get_ip_from_log(file_name):
    try:
        file = open(file_name, 'r')
        content = file.readlines()
    except IOError:
        print('Unexpected error: something went wrong with ' + file_name)
        return

    ip_addresses = []
    for line in content:
        line_content = line.split('   ')
        if line_content[1] not in ip_addresses:
            ip_addresses.append(line_content[1])

    return ip_addresses

print(len(get_ip_from_log('log.txt')))


