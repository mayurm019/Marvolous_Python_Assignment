# Calculate Squre and Cube of Given number using lambda function


def main():

    print("Enter the number: ")
    no = int(input())

    Squre =  lambda  no : (no * no)
    ret = Squre(no)

    Cube = lambda  no : (no**3)
    ans = Cube(no)

    print(F"Squre of Given number {no} is : ", ret)
    print(F"Cube of Given number {no} is :", ans)


if __name__ == "__main__":
    main()