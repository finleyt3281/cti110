# CTI-110
# P3HW2 - Salary
# Tarquin Finley
# 3/23/2023
#

name = input("Enter Employeer's name: ")
hours = float(input("Enter number of hour's worked: "))
payrate = float(input("Enter employee's payrate: "))

ovrhrs = 0.0
ovrpay = 0.0

if hours > 40:
    regpay = payrate * 40
    ovrhrs = hours - 40
    ovrpay= payrate * ovrhrs * 1.5
    grosspay = ovrpay + regpay

else:
    regpay = hours * payrate
    grosspay = ovrpay + regpay
print("-"*50)
print('Employee name:', name)    

print()
print("Hours Worked"+" "*5 +"Pay Rate"+" "*5 +"Overtime"+" "*5 +"Overtime Pay"+" "*5 +"RegHour Pay"+" "*5 +"Gross Pay")
print("-"*150)

print(hours,'\t\t',payrate,'\t',ovrhrs,'\t'+'$' + str(format(ovrpay,',.2f')) +'\t\t'+'$'+str(format(regpay,',.2f')) + '\t'+ '  $' +  str(format(grosspay, ',.2f')))
    
