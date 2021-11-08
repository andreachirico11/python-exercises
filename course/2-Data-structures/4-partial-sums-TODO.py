# 4. Partial Sums
# Take a list l of numbers (bound it to a variable),
# and write a program that prints the array res of the partial sums of l computed in the following way.
# • The first element of res is the first element of l
# • The second element of res is the summation from the second to the third element of l
# • The third element of res is the summation from the fourth to the sixth element of l
# • The fourth element of res is the summation from the seventh to the tenth element of l and so on...
# • If the summation could not be completed because l ends just truncate the summation.
#     e.g.,-l =[1, 5, 6],res =[1, 11]-l =[1, 5, 6, 1, 1, 1, 2, 2, 2, 2],res =[1, 11, 3,8]-l=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6],res=[1, 4, 9, 16, 11]
