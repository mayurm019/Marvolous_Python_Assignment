# 5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#  Filter should filter out all prime numbers. 
# Map function will multiply each number by 2.
#Reduce will return Maximum number from that numbers.
#You can also use normal functions instead of lambda functions).
from functools import reduce
def is_prime(n):
    if (n <  2):
        return False
    for i in range(2,int(n**0.5)+1):

        if n%i ==0:
            return False
    return True   
    
Input_List = [2, 70 , 11, 10, 17, 23, 31, 77]

filt = list(filter(lambda x : is_prime(x), Input_List))
print(filt)

maped = list(map(lambda x :x*2, filt ))
print(maped)

red = reduce(lambda x,y: max(x,y),maped)
print(red)