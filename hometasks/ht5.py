# #task 1
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# evenSum = 0
# unEvenSum = 0
# evenNum = 0
# unEvenNum = 0
# divNineSum = 0
# divNineNum = 0
# for i in range(num1, num2):
#     if i // 2 == 0:
#         evenSum += i
#         evenNum += 1
#     else:
#         unEvenSum += i
#         unEvenNum += 1
#     if i // 9 == 0:
#         divNineSum += i
#         divNineNum += 1

# print('Sum of even numbers: ', evenSum)
# print('Sum of uneven numbers: ', unEvenSum)
# print('Sum of numbers divideable 9 numbers: ', divNineSum)
# print('Average of even numbers: ', evenSum / evenNum)
# print('Average of uneven numbers: ', unEvenSum / unEvenNum)
# print('Average of numbers divideable 9 numbers: ', divNineSum / divNineNum)

# #task 2
# length = int(input('Enter length of your line: '))
# sym = input('Enter the symbol to fill your line: ')
# for i in range(1, length + 1):
#     print(sym)

# #task 3
# num = int(input('Enter any number: '))
# if num == 7:
#     print('Goodbye!')
# elif num < 0:
#     print('Number is negative')
# elif num == 0:
#     print('Number is equal to zero')
# elif num < 0:
#     print('Number is positive')

#task 4
while True:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    if (num1 == 7) or (num2 == 7):
        print('Goodbye!')
        break

    else:
        print('The sum of numbers: ', num1 + num2)

        if num1 > num2:
            print('The maximum number: ', num1)
            print('The minimum number: ', num2)
        
        elif num2 > num1:
            print('The maximum number: ', num2)
            print('The minimum number: ', num1)