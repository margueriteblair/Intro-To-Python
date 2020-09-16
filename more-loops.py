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