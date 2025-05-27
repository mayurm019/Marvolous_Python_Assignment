# create list from user input and double list item using map data

Double = lambda  no:(no*2)

def main():
    List = []

    print("Enter the number or elements: ")
    no = int(input())

    for i in range (no):
        Num = int(input(f"Enter element {i+1}: "))
        List.append(Num)
    print(List)

    ans = list(map(Double, List))
    print("The answer for Map function is: ", ans)

if __name__ == "__main__":
    main()
