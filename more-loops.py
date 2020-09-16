#counting in a loop, 

zork = 0
print('Before', zork)
for thing in [9, 42,12, 3, 74, 15]:
    zork = zork+1
    print(zork, thing)
print('After', zork)

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 42,12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', sum, count, sum/count)

#we can also use Boolean values to search for things 

found = False
print('Before', found)
for value in [9, 42,12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#none type has one marker None, it's a constant
# is is stronger than equal sign

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print('AFTER', smallest)

#python has an is operator that can be used in logical expressions
#is implies 'is the same as'
#is not is also a logical operator
