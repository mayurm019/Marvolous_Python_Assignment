# create list from user input and multiplication of  list item using reduce function 

from functools import reduce

Multiplication = lambda A,B : A*B

def main():
    List = []

    print("Enter the number or elements: ")
    no = int(input())
    
    for i in range (no):
        Num = int(input(f"Enter element {i+1}: "))
        List.append(Num)
    print("Your updated list is", List)

    ans = reduce(Multiplication,List)
    print("The answer for reduce function is: ", ans)

if __name__ == "__main__":
    main()
