# This program is to print Prime number or not

# def CheckPrime(no):
#     if no <= 1:
#         print("Number is not prime")
#     for i in range(2, int(no ** 0.5) + 1):
#         if no % i == 0:
#             print("Number is not prime")
# #     return True
#     print("Number is prime")


def main():
      print("Enter number")
      no = int(input())
      if no <= 1:
        print("Number is not prime")
      for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            print("Number is not prime")
#     return True
      print("Number is prime")
    
if __name__ == "__main__":
    main()