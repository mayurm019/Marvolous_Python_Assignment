def ChkNum(val):
    
    num = (val % 2)
    return num
    # if (num == 0):
    #     print('Even Number')
    # else:
    #     print("Odd Number")
    # return num
   
def main():
    print("Enter The Number")
    val = int(input())  
    result = ChkNum(val)
    if (result == 0):
        print('The Given number is Even Number', val)
    else:
        print("The Given number is Odd Number", val)
    
    print('The number is:', result)



if __name__ == '__main__':
    main()
