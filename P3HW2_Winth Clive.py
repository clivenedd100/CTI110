#CTI-110
#P3HW2 - Salary
#Clive Winth
#10/29/2022
#

#Pseudocode :

'''

name = input ask user Enter employee's name
hours = input ask Enter worked hours
payrate = input ask Enter pay rate


set overtime pay = 132.25
set over_time = 5.0


if hours greater than 40
do the evaluation of the overtime pay and regular pay
        over_time = hours_worked - 40
        ot_payrate = pay_rate + (pay_rate * 0.5)
        overTime_pay = over_time * ot_payrate
        reg_pay = 40 * pay_rate

else
do the evaluation of the regular pay
reg_pay = hours_worked * pay_rate


And then calculate the gross pay = regular pay + overtime pay

print output
'''

#('This program  assess student understanding of decision structures')

#to read data from user
Employee_name = input("Enter employee's name:")

hours_worked = float(input('Enter number of hours worked:'))

Employee_payrate = float(input("Enter employee's pay rate:"))
#To calculate total pay(overtime and regular pay)
overtime= hours_worked-40
regpay= (hours_worked-overtime)*Employee_payrate
overtimepayrate=26.25
overtimepay=overtime*overtimepayrate
gross= regpay+overtimepay
#To print
print('---------------------------------------------------')
print('Employee Name:       ',Employee_name)
print('')
print('Hours Worked      Pay Rate        OverTime       OverTime Pay        RegHour Pay        Gross Pay')
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print(hours_worked,'            ',Employee_payrate,'          ',overtime,'          ',overtimepay,'          ','$',regpay,'           ','$',gross)
