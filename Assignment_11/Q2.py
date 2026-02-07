# Write a recursive function to calculate factorial of a number.
# factorial(5) → 120

def Factorial(n):
    if n <=1:
        return 1
    return n * Factorial(n-1)

n = int(input("Enter te number : "))
res = Factorial(n)
print(res)