# Create List from user input and find minimum number from list 
def MinNum(List):
    Min = List[0]
    for number in List:
        if  number < Min:
            Min = number
    return Min


def main():
   
    List = []
    print("Enter the number or elements: ")
    val = int(input())

    for i in range(val):
        Num = int(input(i+1))
        List.append(Num)
        # return List
    print(List)

    print("Enter the number : ")
    val1 = int(input())
    value = 0
    for j in List:
        if j == val1:
            value = value + 1

    
    print(f"Occurence of Number {val1} in given list element is :",value)

if __name__ == "__main__":
    main()