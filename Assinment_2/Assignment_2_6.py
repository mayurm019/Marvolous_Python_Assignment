# Accept one number and display te pattern

def main():
    print('Enter the range')
    n = int(input())
    for i in range(n, 0, -1):
        print("*" * i)

if __name__ == "__main__":
    main()

