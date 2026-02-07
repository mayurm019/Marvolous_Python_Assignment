# Write a recursive function to calculate the sum of digits of a number.
# sum_of_digits(1234) → 10

def sum_of_digits(n):
    total = 0
    for i in (n):
       
       total += int(i)
    return total
    
no = int(input("entre number"))
n = str(no)
res = sum_of_digits(n)
print(res)



