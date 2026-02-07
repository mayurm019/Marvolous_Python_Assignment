import threading

def Even(no):
    
    # for i in range(2,no+1):
    #     even = (i % 2)
    #     if even == 0:
    #         print(i)
    #     i = i + 1 

    i = 1
    while (i <= 10):
        print(i * 2)
        i = i +1 

def Odd(no):
    # print('Odd Numbers are below')
    for i in range(1,no+1):
        odd = i % 2
        if odd != 0:
            print(i)
        i = i + 1 



def main():

    print('Even Numbers are below')
    T1 = threading.Thread(target=Even, args=(20,))
    T1.start()
    T1.join()
    print('Odd Numbers are below')
    T2 = threading.Thread(target=Odd, args=(20,))
    T2.start()
    T2.join()


if __name__ == '__main__':
    main()