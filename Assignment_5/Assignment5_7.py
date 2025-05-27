# Find Area And Perimeter of Rectangle
def Area(Len,wid):
    A =  Len * wid 
    return A

def Perimeter(Len,wid):
    P = 2 * (Len * wid)
    return P

def main():

    print("Enter Legth of Rectangle :")
    Len = int(input())

    print("Enter Width of Rectangle :")
    wid = int(input())

    result1 = Area(Len,wid)  
    print("The Area of Rectangle is: ",result1)

    result2 = Perimeter(Len,wid)  
    print("The Perimeter of Rectangle is: ",result2)
    
if __name__ == '__main__':
    main()
