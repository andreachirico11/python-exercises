# Assign the first element of the list to answer_1 on line 2
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]

print(answer_1)


# And let's print the second element directly inside print function.
# This time print the second element of the list directly on line 3. You should get 100.

lst = [11, 100, 101, 999, 1001]

print(lst[1])


# And the last element.
# Print the last element of the list through variable answer_1.
lst = [11, 100, 101, 999, 1001]
answer_1 = lst[-1]

print(answer_1)


# .append method will let you add items to your lists.
# On line 3, add the string "pajamas" to the list with .append() method.
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append('dgfhjasjlkfdds')
print(gift_list)


# Lists can hold many type of data inside them. You can even add another list to a list as its element.
# This is called nested data in Python.
# On line 3, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.
gift_list_2 = ['socks', '4K drone', 'wine', 'jam']
gift_list_2.append(['a', 1])
print(gift_list_2)


# .insert() lets you specify the index you want to add your item.
# On line 3, this time insert "slippers" to index 3 of gift_list.
gift_list_3 = ['socks', '4K drone', 'wine', 'jam']
gift_list_3.insert(2, 'xxx')
print(gift_list_3)


# With .index() method you can learn the index number of an item inside your list.
# Assign the index no of 8679 to the variable answer_1.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print(answer_1)


# Using .remove() method, clear the last element of the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.remove(99)
print(lst)

# Using .reverse() method, reverse the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.reverse()
print(lst)


# Using .count() method, count how many times 6 occur in the list.
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = lst.count(6)
print(answer_1)


# What is the sum of all the numbers in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = sum(lst)
print(answer_1)


# What is the minimum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = max(lst)
print(answer_1)
