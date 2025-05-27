# Accept Characters from user and and display as its Vowel or Consonant


def main():
    print("Enter Character :")
    char = input()

    if  (char == 'a' or char == 'e' or
        char == 'i' or char == 'o' or char == 'u'):
            print("Given input is Vowel")
    else:
            print("Given input is Consonant")
    

if __name__ == '__main__':
    main()
