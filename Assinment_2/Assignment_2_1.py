import Arithmatic1 as Algebra
# from Assignment_2_1 import Arithmatic1
def main():
    print('Enter First value')
    val1 = int(input())
    print('Enter First value')
    val2 = int(input())

    result = Algebra.Add(val1,val2)
    print(f'Addition of given number {val1} and {val2} is:', result)

    result = Algebra.Sub(val1,val2)
    print(f'Substraction of given number {val1} and {val2} is:', result)

    result = Algebra.Div(val1,val2)
    print(f'Division of given number {val1} and {val2} is:', result)

    result = Algebra.Mult(val1,val2)
    print(f'Multiplication of given number {val1} and {val2} is:', result)


if __name__ == "__main__":
    main()

