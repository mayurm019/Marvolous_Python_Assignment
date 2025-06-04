# Find Factorial of user input value

def main():
    print('Enter number')
    val = int(input())
    fact = 1
    for i in range(1, val + 1):
        fact = fact * i
    print(f"Factorial of {val} is :", fact)

    
if __name__ == "__main__":
    main()

