# Write a recursive function to calculate x^n.

# Power Function Using Recursion


def Power_Function(x , n):
    if x == 0:
        return 0
    # elif(n==0):
    #     return 1
    else:
        ans = x**n
        return ans

# def Power_Function(x , n):
#     if n == 0:
#         return 1
#     return x*Power_Function(x,n-1)

x = int(input("enter number : "))
n = int(input("enter Power : "))

res = Power_Function(x,n)
print(res)
