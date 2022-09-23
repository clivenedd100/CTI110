print('Travel Expenses')
print('09/21/2022')
print('CTI-110 P1HW2 - Travel Expenses')
print('Clive Winth')

print ('This program calculates and displays travel expenses') 
budget = int(input('Enter Budget:\n'))

dest = str(input('Enter travel destination:\n'))

gas =int(input('How much do you think you will spend on fuel?:\n'))

acc =int(input('Approximately, much do you think you will spend on accommodation/hotel?:\n'))

food =int(input('Last, how much do you need for food:\n'))


print ('------------- Travel Expenses---------------------') 
print ('Location:', dest) 

print ('Initial Budget:', budget)


print ('Fuel:', gas)
print ('Accommodation:', acc)
print ('Food:', food)

print('Remaining balance:',budget - gas - acc- food)
