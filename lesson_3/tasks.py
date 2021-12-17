 #task 1
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = 0

print((num1 + num2) / 2)
print()
for i in range(num1, num2 + 1):
    num3 += i

print(num3)

#task 2
num = int(input('Enter any positive number: '))
fact = 1

if num > 0:
    for i in range(1, num + 1):
        fact *= i
else:
    print('Only positive numbers allowed!')

print(fact)

#task 3
num = int(input('Enter length of star line: '))
print(num * '*')

# task 4
num = int(input('Enter length of your line: '))
sym = input('Enter symbol of line: ')
print(num * sym)

#task 5
num = int(input('Enter number: '))
print(num, '* 1', '=', num * 1)
print(num, '* 2', '=', num * 2)
print(num, '* 3', '=', num * 3)
print(num, '* 4', '=', num * 4)
print(num, '* 5', '=', num * 5)
print(num, '* 6', '=', num * 6)
print(num, '* 7', '=', num * 7)
print(num, '* 8', '=', num * 8)
print(num, '* 9', '=', num * 9)
print(num, '* 10', '=', num * 10)

dollar = 73.46
euro = 82.96
bitcoin = 3518017.30

while True:
    convert = int(input('Choose operation:\n1 - Convert USD-RUB\n2 - Convert EUR-RUB\n3 - Convert BTC-RUB\n'))

    if convert == 1:
        raw_value = int(input('Choose your value:\n1 - USD\n2 - RUB\n'))
        if raw_value == 1:
            value = int(input('Enter your sum: '))
            print(value * dollar)
        elif raw_value == 2:
            value = int(input('Enter your sum: '))
            print(value / dollar)
        else:
            print('Incorrect value chosen. Try again.')
    elif convert == 2:
        raw_value = int(input('Choose your value:\n1 - EUR\n2 - RUB\n'))
        if raw_value == 1:
            value = int(input('Enter your sum: '))
            print(value * euro)
        elif raw_value == 2:
            value = int(input('Enter your sum: '))
            print(value / euro)
        else:
            print('Incorrect value chosen. Try again.')
    elif convert == 3:
        raw_value = int(input('Choose your value:\n1 - BTC\n2 - RUB\n'))
        if raw_value == 1:
            value = int(input('Enter your sum: '))
            print(value * bitcoin)
        elif raw_value == 2:
            value = int(input('Enter your sum: '))
            print(value / bitcoin)
        else:
            print('Incorrect value chosen. Try again.')
    
    else:
        print('Incorrect value chosen. Try again.')

#task 3
border1 = int(input('Enter 1st number: '))
border2 = int(input('Enter 2nd number: '))

while True:
    num = int(input('Enter any number: '))

    list = []
    if (num > border1) and (num < border2):
        for i in range(border1, border2 + 1):
            list.append(i)
            if num == i:
                list[list.index(i)] = '!' + str(list[list.index(i)]) + '!'
        print(list)
    else:
        print('Number is not between the borders')