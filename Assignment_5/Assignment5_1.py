# Accept Two integers from user and and display their Addition, Substraction, Division, Multiplication using conditional logic
#

import sys

def Addition(no1,no2):
    sum = 0
    sum = no1 + no2
    return sum

def Substraction(no1,no2):
    sub = 0
    sub = no1 - no2
    return sub
   
def Division(no1,no2):
    div = 0
    div = no1 / no2
    return div

def Multiplication(no1,no2):
    mult = 0
    mult = no1 * no2
    return mult

def main():
    no1 = int(sys.argv[1])  
    no2 = int(sys.argv[2])  

    result1 = Addition(no1,no2)
    print("The addition of given numbers is: ", result1)

    result2 = Substraction(no1,no2)
    print("The Substraction of given numbers is: ", result2)

    result3 = Division(no1,no2)
    print("The Division of given numbers is: ", result3)

    result4 = Multiplication(no1,no2)
    print("The Multiplication of given numbers is: ", result4)

if __name__ == '__main__':
    main()
