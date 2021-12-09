#task 1
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
oper = input('Choose operation(sum, mult): ')
if oper == 'sum':
    print(num1 + num2 + num3)
elif oper == 'mult':
        print(num1 * num2 *num3)
else:
    print('Incorrect operation. Try again.')

#task 2
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
oper = input('Choose operation(max, min, aver): ')
if oper == 'max':
    if (num1 > num2) and (num1 > num3):
        print(num1)
    elif (num2 > num1) and (num2 > num3):
        print(num2)
    elif (num3 > num1) and (num3 > num2):
        print(num3)
    else:
        print('Don\'t use same numbers!')
elif oper == 'min':
    if (num1 < num2) and (num1 < num3):
        print(num1)
    elif (num2 < num1) and (num2 < num3):
        print(num2)
    elif (num3 < num1) and (num3 < num2):
        print(num3)
    else:
        print('Don\'t use same numbers!')
elif oper == 'aver':
    print((num1 + num2 + num3) / 3)
else:
    print('Incorrect operation. Try again.')

#task3
met = int(input('Enter length in meters: '))
unit = input('Choose new unit(miles, inches, yards): ')
if unit == 'miles':
    print(met / 1609)
elif unit == 'inches':
    print(met * 39.37)
elif unit == 'yards':
    print(met * 1.094)
else:
    print('Incorrect unit. Try again.')
