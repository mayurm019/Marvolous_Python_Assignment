# This program is to print 1-50 using while loop

def main():

    sum = 0
    for i in range(0,100,2):
        sum = sum + i
    print("Addition of Even numbers from 1 to 100 is :", sum)

if __name__ == "__main__":
    main()