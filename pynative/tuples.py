# Exercise 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
temp_list = list(aTuple)
temp_list.reverse()
aTuple = (temp_list)
print(aTuple)

# Exercise 2: Access value 20 from the following tuple
bTuple = ("Orange", [10, 20, 30], (5, 15, 25))

print(bTuple[1][1])


# Exercise 3: Create a tuple with single item 50
print(type((50,)))

# Exercise 4: Unpack the following tuple into 4 variables
cTuple = (10, 20, 30, 40)
a, b, c, d = cTuple
print(a, b, c, d)


# Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1, tuple2)


# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
dTuple = (11, 22, 33, 44, 55, 66)
print(tuple(dTuple[3:5]))

# Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
eTuple = (11, [22, 33], 44, 55)
eTuple = (eTuple[0: 1] + ([222, eTuple[1][1]],) + eTuple[2:])
print(eTuple)


# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple123 = (50, 10, 60, 70, 50)
print(tuple123.count(50))


# Exercise 10: Check if all items in the following tuple are the same
tup = (45, 45, 45, 45)

print(all(tup))
