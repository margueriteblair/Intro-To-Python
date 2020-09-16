#a list is pythons version of an array
#list:
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

#a llist can also be empty

list2 = [1, 2, 3, [4, 5], 6] #lists can be made up of other lists
print(list2)
#strings are immutable

list2[3] = 5
print(list2)

length = len(list2)

#range(len(list2))

friends = ["Margie", "Chelsea", "Will"]
for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)