# This program is to print Prime number or not

def main():
    print("enter number for multiplication")
    no = int(input())
    Fact = (no % 2)
    if Fact == 1 or Fact == no:
        print("The given number is Prime number")
    else:
        print("The given number is Not Prime number")

    
if __name__ == "__main__":
    main()