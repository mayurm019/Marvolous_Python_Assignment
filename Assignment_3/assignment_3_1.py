# 1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.


def main():
   
    Data = []
    print("Enter the number or elements: ")
    val = int(input())

    for i in range(val):
        Num = int(input(f"Enter number {i+1}:"))   #user count start from 1 and iteration start from 0 so user perspective start from1
        Data.append(Num)
    print(Data)

    Addition = sum(Data)
    print(f"Addition of given list element {Data} is :",Addition)

if __name__ == "__main__":
    main()