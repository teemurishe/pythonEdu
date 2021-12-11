# #task 1
# num = int(input('Enter first number (from 1 to 100): '))

# if (num < 1) or (num > 100):
#     print('Incorrect numbers! Only numbers from 1 to are allowed')
# else:
#     if (num % 3 != 0) and (num % 5 != 0):
#         print(num)
#     elif (num % 3 == 0) and (num % 5 == 0):
#         print('Fizz Buzz')
#     elif (num % 3 == 0) and (num % 5 != 0):
#         print('Fizz')
#     elif (num % 3 != 0) and (num % 5 == 0):
#         print('Buzz')

#task 2
num = int(input('Enter any number: '))
degree = int(input('Enter degree (from 1 to 7): '))
if (degree < 1) or (degree > 7):
    print('Incorrect degree. Choose degree from 1 to 7')
else:
    if degree == 1:
        print(num)
    elif degree == 2:
        print(num * num)
    elif degree == 3:
        print(num * num * num)
    elif degree == 4:
        print(num * num * num * num)
    elif degree == 5:
        print(num * num * num * num * num)
    elif degree == 6:
        print(num * num* num* num * num * num)
    elif degree == 7:
        print(num * num * num * num * num * num * num)