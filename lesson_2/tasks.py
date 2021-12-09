# #task 1
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))

# for i in range(num1, num2 + 1):
#     print(i)

# #task 2
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))

# for i in range(num1, num2 + 1):
#     if (i % 2 != 0):
#         print(i)

# #task 3
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))

# for i in range(num1, num2 + 1):
#     if (i % 2 == 0):
#         print(i)

# #task 4
# #Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке убывания
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# for i in range(num2, num1 - 1, -1):
#     print(i)

# task 5
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# if num1 < num2:
#     for i in range(num1, num2 + 1):
#         if (i % 2 != 0):
#             print(i)
# elif num1 > num2:
#     for i in range(num2, num1 + 1):
#         if (i % 2 != 0):
#             print(i)
# else:
#     if num1 % 2 !=0:
#         print(num1)
#     else:
#         while True:
#             break

# #task 6
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# num3 = 0

# print((num1 + num2) / 2)
# print()
# for i in range(num1, num2 + 1):
#     num3 += i

# print(num3)

#task 7
num = int(input('Enter any positive number: '))
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)