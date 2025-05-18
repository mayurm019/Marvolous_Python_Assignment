# Print strin multiple time

def main():
    print('enter number as how much time you have to repeate')
    print("Print number in parallel")
    x = int(input())
    for a in range(x):
        print('*')

    print("Print number in series")
    print("* " * x)

if __name__ == '__main__':
    main()