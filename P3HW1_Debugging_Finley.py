# CTI-110
# P3HW3
# Tarquin Finley
# 3/21/2023
#

# Enter grades for six modules
grades = [ ]
mod_1 = float (input ("Enter grade for Module 1: "))
mod_2 = float (input ("Enter grade for Module 2: "))
mod_3 = float (input ("Enter grade for Module 3: "))
mod_4 = float (input ("Enter grade for Module 4: "))
mod_5= float (input ("Enter grade for Module 5: "))
mod_6 = float (input ("Enter grade for Module 6: "))

# add grades to entered list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest, sum and average for grades


low = min(grades)
max = max(grades)
sum = sum(grades)
avg = sum / len(grades)

#determine letter grade for average

if avg >= 90:
    grade= 'A'
else:
    if avg >= 80:
        grade= 'B'
    else:
        if avg >= 70:
            grade= 'C'
        else:
            if avg >= 60:
                grade= 'D'
            else:
                grade= 'F'


print ( '-' * 12, 'Results', '-' * 12)

print ('Lowest Grade: '+ str(format(low ,',.2f' )).rjust(15))
print ('Highest Grade: '+ str(format(max ,',.2f')).rjust(15))
print ('Sum of Grade: '+ str(format(sum ,',.2f')).rjust(16))
print ('Average: ' + str(format(avg , ',.2f')).rjust(26))

print( '-' *40)

print('Your grade is: ' + grade)
          
