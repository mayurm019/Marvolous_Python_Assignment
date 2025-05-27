# To check Entered no is Odd or Even

def main():
    print("Enter number :")
    no1 = int(input())
    num = 0
    num = (no1 % 2)
  
    if   (num == 0):
        print("Number Is Even :", no1)
    else:
        print("Number Is ODD :", no1)

if __name__ == '__main__':
    main()
