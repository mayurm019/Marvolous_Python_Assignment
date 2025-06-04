
# Accept user input and print pattern 
def main():
    print('Enter range to print pattern')
    val1 = int(input())
    for i in range(1, val1+1):
        for j in range(1, val1+1):
        
            print("*", end= " ")
        print()

if __name__ == "__main__":
    main()

