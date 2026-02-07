# 4.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers.

from functools import reduce
List_1 = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

Filt = list(filter(lambda x:x%2==0,List_1))
print(Filt)

Maped = list(map (lambda x : x**2 , Filt))
print(Maped)

red = reduce(lambda a,b  : a+b, Maped)
print(red)