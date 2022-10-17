#print('Travel Expenses')
#print('10/6/2022')
#print('CTI-110 P2HW1 - Travel Expenses')
#print('Clive Winth')
#

('This program calculates and displays travel expenses')
#This section covers the  user input and formatting
print('Enter Budget:\n')
budget = int(input())

print('Enter travel destination:\n')
dest = input()

print('How much do you think you will spend on fuel?:\n')
gas = int(input())

print('Approximately, much do you think you will spend on accommodation/hotel?:\n')
acc = int(input())

print('Last, how much do you need for food:\n')
food = int(input())

#This section display the input from user 
print('------------- Travel Expenses---------------------') 
print('Location:                 ',dest) 
  
print(f'Initial Budget:            ${budget:.1f}')


print(f'Fuel:                      ${gas:.1f}')
print(f'Accommodation:             ${acc:.1f}')
print(f'Food:                      ${food:.1f}')

print('--------------------------------------------------')
#This is the conclusion of this programme
print(f'Remaining balance:         ${budget-gas-acc- food:.1f}')








