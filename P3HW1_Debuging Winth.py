# CTI-110
# P2HW2 - Debugging
# WInth CLive
# 10/25/2022
#

#('This program asks a user for a list of grades, displays the highest and lowest grade. Then, calculates the sum and average of all grades.')
# Enter grades for six modules
Mod_1 = float(input('Enter grade for Module 1: '))
Mod_2 = float(input('Enter grade for Module 2: '))
Mod_3 = float(input('Enter grade for Module 3: '))
Mod_4 = float(input('Enter grade for Module 4: '))
Mod_5 = float(input('Enter grade for Module 5: '))
Mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

Grades = list([Mod_1, Mod_2, Mod_3, Mod_4, Mod_5, Mod_6])

# TO DO: determine lowest, highest , sum and average for grades

total = (Mod_1 + Mod_2 + Mod_3 + Mod_4 + Mod_5 + Mod_6)
def highestNumber(l):
    myMax = float(0)
    for i in l:
        if i > myMax:
            myMax = i
    return myMax
def lowestNumber(l):
    myMin = float(100)
    for i in l:
        if i < myMin:
            myMin = i
    return myMin
low = lowestNumber(Grades)
high = highestNumber(Grades)
average = (total/6)
rounded_average = round(average, 2)

print('---------------Results---------------')
print('Lowest Grade:              ', low)
print('Highest Grade:             ', high)
print ('Sum of Grades:             ', total)
print ('Average:                   ', rounded_average)
print('-------------------------------------')

#final grade of modules
Your_grade = input('Your grade: B')
grade = input()



