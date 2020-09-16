#we want to be able to work outside of our code
#we want to work on files
#a text file can be thought of as a sequence of lines
#a textfile implicitly has a bunch of newline markers at the end of each line

#handle = open(filename, mode)
# you pass in a file, then tell you if you want to read or write
#UTF-8
#\n indicates a new line
stuff = 'X\nY'
print(stuff)
handle = open("stuff.txt", "read")