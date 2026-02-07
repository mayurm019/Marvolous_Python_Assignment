import threading

def EvenFactor(no):
    sum = 0
    for i in range(1,no+1):
        even = (i % 2)
        if even == 0:
            print(i)
            sum = sum + i
        i = i + 1
    print("Addition of Even Factor of given Number is :",sum)
        # sum = sum + 1


def OddFactor(no):
    sum = 0
    for i in range(1,no+1):
        odd = i % 2
        if odd != 0:
            sum = sum + i
            print(i)
        i = i + 1
    print("Addition of Odd Factor of given Number is :",sum) 



def main():

    print('Enter the number:')
    no = int(input())

    print('Even Numbers are below')
    T1 = threading.Thread(target=EvenFactor, args=(no,))
    # print("Addition of Even Factor of given Number is :",sum)
    T1.start()
    T1.join()
    print('Odd Numbers are below')
    T2 = threading.Thread(target=OddFactor, args=(no,))
    T2.start()
    T2.join()


if __name__ == '__main__':
    main()