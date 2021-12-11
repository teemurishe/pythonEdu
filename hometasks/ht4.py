#task 1
num = int(input('Enter first number (from 1 to 100): '))

if (num < 1) or (num > 100):
    print('Incorrect numbers! Only numbers from 1 to are allowed')
else:
    if (num % 3 != 0) and (num % 5 != 0):
        print(num)
    elif (num % 3 == 0) and (num % 5 == 0):
        print('Fizz Buzz')
    elif (num % 3 == 0) and (num % 5 != 0):
        print('Fizz')
    elif (num % 3 != 0) and (num % 5 == 0):
        print('Buzz')