# Create a method called decryptDoubled() that takes a filename as string as a parameter
# and it can decrypt the duplicated-chars.txt file
# Decryption is the process reversing an encryption, i.e. the process
# which converts encrypted data into its original form.
# If the file can't be opened it should return this message: File not found
# The result should be saved in the output.txt file

def decrypt(file_name):
    content = ''
    new_content = ''

    try:
       file = open(file_name, 'r')
       content = file.read()
    except IOError:
        print('Loading error: unable to read file')

    for i in range(len(content)):
        if i%2 == 0:
            new_content += content[i]

    try:
        decrypted_file = open('output.txt3', 'w')
        decrypted_file.write(new_content)
    except IOError:
        print('Loading error: unable to write file')


decrypt('doubled.txt')


