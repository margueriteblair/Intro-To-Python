n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')
print(n)

#be sure not to create infinit loops in python either

#if the condition is never met in a python while loop, they'll be skipped over

while True:
    line = input('> ')
    if line == "done":
        break
    print(line)
print('Done!')

#continue says go back up to the top of the loop
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == 'done':
        break
    print(line)
print('Done!')