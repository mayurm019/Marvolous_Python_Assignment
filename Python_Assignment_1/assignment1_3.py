# This code is for get 2 numbers from user and display addition of that 2  numbers

def Add(val1, val2):
    
    sum = val1 + val2
    return sum
  
def main():
    print("Enter The first Number :")
    no1 = int(input())  
    print("Enter The second Number :")
    no2 = int(input())  
    result = Add(no1,no2)
    print('Addition of numbers is: ', result)

if __name__ == '__main__':
    main()
