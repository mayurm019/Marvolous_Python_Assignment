# Accept Age from user and Check Eligibility of Voter 

def main():
    print("Enter Your Age :")
    age = int(input())

    if  age >= 18:
            print("You are eligible for Voting")
    else:
            print("You are Not eligible for Voting")
    

if __name__ == '__main__':
    main()
