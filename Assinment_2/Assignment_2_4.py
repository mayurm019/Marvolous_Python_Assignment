# Take input from user and find factor of it        

def main():
    print('Enter number')
    val = int(input())
    Add = 0
    for i in range(1, val + 1):
        Add = Add + i
    print(f"Addition of number {val} factors is :", Add)

    
if __name__ == "__main__":              
    main()

