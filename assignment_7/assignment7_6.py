# create list from user input and multiplication of  list item using reduce function 

from functools import reduce

def CheckPrime(no):
    if no <= 1:
        return False
    for i in range(2, int(no**0.5) + 1):              #int(no**0.5) for squre root
        if no % i == 0:
            return False
    return True

def main():
    List = []

    print("Enter the number or elements: ")
    no = int(input())
    
    for i in range (no):
        Num = int(input(f"Enter element {i+1}: "))
        List.append(Num)
    print("Your updated list is", List)

    ans = list(filter(CheckPrime,List))
    print("The answer for Filter function is: ", ans)

if __name__ == "__main__":
    main()
