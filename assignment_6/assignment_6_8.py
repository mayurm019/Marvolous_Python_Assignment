
# Get 5 values from the user and find the largest number

def main():
   
    numbers = []

    for i in range(5):
        num = int(input(i + 1))
        numbers.append(num)

    largest = max(numbers)

    print("The largest number is:", largest)

    
if __name__ == "__main__":
    main()