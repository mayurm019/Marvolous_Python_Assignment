# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10.
#  Reduce will return product of all that  numbers.

from functools import reduce

num_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

filt = list(filter(lambda x : 90 >= x >= 70, num_list))
print(filt)


maped = list(map(lambda x : x+10 ,filt))
print(maped)

red = reduce(lambda a,b : a*b,maped)
print(red)



