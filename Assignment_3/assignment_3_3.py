# 3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.


def MinNum(Data):
    Min = Data[0]
    for number in Data:
        if  number < Min:
            Min = number
    return Min


# Option : 2
    # Data.sort()
    # return (Data[-1])


def main():
   
    Data = []
    print("Enter the number or elements: ")
    val = int(input())

    for i in range(val):
        Num = int(input(i+1))
        Data.append(Num)
        # return List
    print(Data)
    
    result  = MinNum(Data)
    print(f"Minimum Number of given list element {Data} is :",result)

if __name__ == "__main__":
    main()