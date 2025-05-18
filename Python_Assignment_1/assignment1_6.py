#   This Program is to check the number is positive negative or Zero 

def main():

    print("Enter the Number :")
    no1 = int(input())  

    if (no1 > 0):
        print('The number is positive')
    elif (no1 < 0):
        print('The number is negative')
    else:
        print('The number is Zero')
  
if __name__ == '__main__':
    main()
