# Write a program that asks the user for a year, and prints whether it is a leap year.
# Hint: a year is a leap (or bissextile) year if it is divisible by 400, or by 4 and not by 100 (e.g., 2000 and
# 2020 were leap years, but 1900 was not).


year = int(input('give the year: '))
print('the year ' + ('is leap' if (year %
      4 == 0 or year % 400 == 0) and year % 100 == 0 else 'isnt leap'))
