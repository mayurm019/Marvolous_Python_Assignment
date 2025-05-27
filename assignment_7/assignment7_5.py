# create list from user input and multiplication of  list item using reduce function 


def main():

    print("Enter the number or Name: ")
    name = input()
    
    result = name[: : -1]
    print(result)
    if result == name:
        print("It is Palindrome")
    else:
        print("It is not Palindrome")
    

if __name__ == "__main__":
    main()
