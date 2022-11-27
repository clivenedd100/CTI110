# 11/26/2022
# CTI-110 P5HW2 - Math Quiz
# Clive Winth
#

import random


# Random module is imported

def addProblem():
    a = random.randint(10,70)
    b = random.randint(10,70)
    # variables (a and b) are displayed to the user with operand '+'
    print(f' {a}')
    print(f'+{b}')
    print('Enter answer.')
    ans = int(input())
    while ans != (a + b):
        if ans < (a + b):
           # A message showing the correct answer should  be displayed 
            print('Sorry, guess is to low.')
        else:
            print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('congradulation!!!! your answer is correct...\n')

# Main Function
def subProblem():
    a = random.randint(10,70)
    b = random.randint(10,70)
    # variables (a and b) are displayed to the user with operand '-'
    print(f' {a}')
    print(f'-{b}')
    print('Enter answer.')
    ans = int(input())
    while ans != (a - b):
        if ans < (a - b):
            # A message showing the correct answer should  be displayed
            print('Sorry, guess is to low.')
        else:
            print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('congradulation!!!! your answer is correct...\n')

    
def main():
    print('Welcome to Math Quiz\n')
# while loop will keep running until user enters the value 3
    while True:
        # menu i is printed
        print('MAIN MENU')
        print('----------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
    
        choice = input('Please choose one of the menu options:')
        if choice == '1':
            addProblem()
            
        elif choice == '2':
            subProblem()

        elif choice == '3':
            print('Thank you for playing ...\nBye!!')
            break

# Main function is called - start of the program
main()
