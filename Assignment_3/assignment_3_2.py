# 2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.


def MaxNum(Data):
    Max = Data[0]
    for number in Data:
        if  number > Max:
            Max = number
    return Max


def main():
   
    Data = []
    print("Enter the number or elements: ")
    val = int(input())

    for i in range(val):
        Num = int(input(f"Enter number {i+1}:")) 
        Data.append(Num)
        # return Data
    print(Data)
    
    result  = MaxNum(Data)
    print(f"Maximum Number of given list element {Data} is :",result)

if __name__ == "__main__":
    main()