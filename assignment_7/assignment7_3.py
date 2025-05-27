# Print only Even numbers from given list using filter

Even = lambda  no:(no %2 == 0)

def main():
    List = []

    print("Enter the number or elements: ")
    no = int(input())

    for i in range (no):
        Num = int(input(f"Enter element {i+1}: "))
        List.append(Num)
    print(List)

    ans = list(filter(Even, List))
    print("The answer for Filter function is: ",ans)

if __name__ == "__main__":
    main()
