# import argv function
from sys import argv

# set argv names
script, filename = argv

# import the file into 'txt'
txt = open(filename)

# print the filename and file content
print "Here's your file %r:" % filename
print txt.read()

# require filename again
print "Type the filename again:"
file_again = raw_input("> ")

# import the file again
txt_again = open(file_again)

# print the file content
print txt_again.read()

txt.close()
txt_again.close()