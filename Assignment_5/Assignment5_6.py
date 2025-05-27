# Convert temprature from celcius to Fahrenheit

def main():
    print("Enter Temprature :")
    temp = float(input())
    F = 0
    F = (temp*(9/5)) + 32
  
    print("The Temprature in Farenheit is: ",F,"F")
if __name__ == '__main__':
    main()
