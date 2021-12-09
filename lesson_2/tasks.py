#task 1
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

for i in range(num1, num2 + 1):
    print(i)

#task 2
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

for i in range(num1, num2 + 1):
    if (i % 2 != 0):
        print(i)

#task 3
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

for i in range(num1, num2 + 1):
    if (i % 2 == 0):
        print(i)

#task 4
#Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке убывания
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
for i in range(num2, num1 - 1, -1):
    print(i)