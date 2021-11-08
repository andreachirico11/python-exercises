# Using type() function assign the type of the variable to answer_1, then print it.
men_stepped_on_the_moon = True

# Type your code here.

answer_1 = type(men_stepped_on_the_moon)


print(answer_1 is type(men_stepped_on_the_moon))


# my_grade variable is a string (because it's in quotes). On line 9, convert it to an integer.

my_grade = "10"

answer_5 = int(my_grade)


print(answer_5)


# my_temp variable is a float (because it has decimals). On line 9, convert it to an integer.

my_temp = 97.70

answer_6 = int(my_temp)


print(answer_6)

# Finally, str will help you convert a data into a string.
gross_world_product = 84.84

gwp_str = str(gross_world_product)

answer_8 = "In 2018 gross product of the world (GWP) was " + \
    gwp_str + " in trillion US dollars."


print(answer_8)
