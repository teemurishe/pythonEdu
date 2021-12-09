#task 1
day = int(input('Number of the day in the week: '))
if day == 1:
    print('The day is Monday')
elif day == 2:
    print('The day is Tuesday')
elif day == 3:
    print('The day is Wednesday')
elif day == 4:
    print('The day is Thursday')
elif day == 5:
    print('The day is Friday')
elif day == 6:
    print('The day is Saturday')
elif day == 7:
    print('The day is Sunday')
else:
    print('Number is incorrect. Please, input number from 1 to 7.')
    
#task 2
month = int(input('Number of the month: '))
if month == 1:
    print('The month is January')
elif month == 2:
    print('The month is February')
elif month == 3:
    print('The month is March')
elif month == 4:
    print('The month is April')
elif month == 5:
    print('The month is May')
elif month == 6:
    print('The month is June')
elif month == 7:
    print('The month is July')
elif month == 8:
    print('The month is August')
elif month == 9:
    print('The month is September')
elif month == 10:
    print('The month is October')
elif month == 11:
    print('The month is November')
elif month == 12:
    print('The month is December')
else:
    print('Number is incorrect. Please, input number from 1 to 12.')
    
#task 3
num = int(input('Input any number: '))
if num > 0:
    print('Number is positive')
elif num == 0:
    print('Number is equal to zero')
elif num < 0:
    print('Number is negative')
else:
    print('Inputted data is incorrect. Please, try again.')
    
#task 4
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
if num1 == num2:
    print('Numbers are equal')
else:
    if num1 < num2:
        print(num1, num2)
    elif num2 < num1:
        print(num2, num1)
