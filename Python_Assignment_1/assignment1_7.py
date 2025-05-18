def Division(val):
    no = (val % 5)
    return no 
   



def main():

    print("Enter The Number 1 :")
    val = int(input())  
    result = Division(val)

    if (result == 0):
        print('The number is divisible by 5 is :', True)
    else:
        print('The number is divisible by 5 is :', False) 
    
    
  
if __name__ == '__main__':
    main()
