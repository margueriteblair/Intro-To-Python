#we want to solve a problem with a loop
#we want the largest or the smallest

#what is the largest number algo

biggest = 0
for i in [3, 41, 12,9, 74, 15]:
    if i > biggest:
        biggest = i

print(biggest)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)