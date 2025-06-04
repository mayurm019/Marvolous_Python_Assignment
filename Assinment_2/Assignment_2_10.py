# Accept one number from user and display sum of its digit

def main():
    print('Enter the range')
    n = input()
    val = len(n)
    sum = 0
    for i in range(1, val+1):
        sum = sum + i
    print(sum)
    

if __name__ == "__main__":
    main()

