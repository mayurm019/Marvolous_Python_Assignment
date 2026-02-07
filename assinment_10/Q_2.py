# 1.Write a program which contains one lambda function which accepts two parameter and return multiplication of two.

n1 = int(input("Enter number1 : " ))
n2 = int(input("Enter number2 : " ))


power =lambda n1,n2:(n1*n2)
result1 = power(n1,n2)

print(result1)