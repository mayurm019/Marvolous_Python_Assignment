# This program is to print Factorial of given number
def main():
    print("enter number for multiplication")
    no = int(input())
    Fact = 1
    for  i  in range(1, no+1):
        Fact = Fact * i
    print(f"Factorial of {no} is :", Fact)

if __name__ == "__main__":
    main()