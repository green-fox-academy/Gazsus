# Write a function that copies the contents of a file into another file
# It should take two filenames as parameters
# It should return a boolean that shows if the copy was successful

import shutil

shutil.copyfile('my-file.txt', 'file.txt')
