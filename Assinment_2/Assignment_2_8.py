# Accept one number and display te pattern

def main():
    print('Enter the range')
    n = int(input())
    j = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='' )
        i = i+1
        print('')

if __name__ == "__main__":
    main()

