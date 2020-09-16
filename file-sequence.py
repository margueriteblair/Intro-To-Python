# we're going to use a python for loop
#our file handle represents a sequence

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

#read as for each line in xfile, run the loop once for every line

#we can count the lines in the file
fhand = open('mbox.txt')
for line in fhand:
    count = count+1
print('Line Count: ', count)