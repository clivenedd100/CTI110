# CTI-110
# P2HW2-list
# Clive Winth
# 10/14/2022
#

#('This program asks a user for a list of grades, displays the highest and lowest grade. Then, calculates the sum and average of all grades.')

Module1 = float(input('Enter grade for Module 1: '))

Module2 = float(input('Enter grade for Module 2: '))

Module3 = float(input('Enter grade for Module 3: '))

Module4 = float(input('Enter grade for Module 4: '))

Module5 = float(input('Enter grade for Module 5: '))

Module6 = float(input('Enter grade for Module 6: '))

# This List function display's the modules in a list
Topics =list([Module1, Module2, Module3, Module4, Module5, Module6])

# this section shows calculations of Modules
total = sum(Topics)
low = min(Topics)
high = max(Topics)
average = (total/6)
rounded_average = round(average, 2)

# This final section shows the end results
print('---------------Results---------------')
print('Lowest Grade:               ', low)
print('Highest Grade:              ', high)
print ('Sum of Grades:              ', total)
print ('Average:                    ', rounded_average)
print('-------------------------------------')
