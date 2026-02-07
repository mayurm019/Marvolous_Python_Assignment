# Write a recursive function to print numbers from 1 to N.

def num(n,current = 1):
    if current > n:
        return 
    print(current)
    num(n, current+1)


res = num(5)
print(res)