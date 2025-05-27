# This program is to print Multiplication of given number upto 10

def main():
    print("enter number for multiplication")
    no = int(input())
    for mult in range(1,11):
        print(no, "*", mult, "=" , no*mult)
    

if __name__ == "__main__":
    main()