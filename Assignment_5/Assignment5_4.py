# FInd The Largest number from user input


def main():
    print("Enter first number :")
    no1 = int(input())
    print("Enter Second number :")
    no2 = int(input())
    print("Enter Third number :")
    no3 = int(input())

    if   (no1 >= no2) and (no1 >= no3):
        print("Largest no is :", no1)
    elif    no2 > no1 and no2 > no3:
        print("Largest no is :", no2)
    else:
        print("Largest no is :", no3)

if __name__ == '__main__':
    main()
