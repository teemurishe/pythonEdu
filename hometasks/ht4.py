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

#task 3
#Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит
#стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
time = int(input('Enter please time of your talk (in minutes): ')) #didn't understand the task: enter cost, choose operators and print cost
#probably, time of dialogue was ment in first input
oper_out = input('Choose your operator (AbobaMobile, DungeonCom): ')
oper_partner = input('Choose your partner\'s operator (same chose): ')
if oper_out == oper_partner: #calls in one network has same tariffs
    print(time * 1.5, 'GBD') #GBD - GachiBoba Dollars
elif (oper_out == 'AbobaMobile') and (oper_partner == 'DungeonCom'):
    print(time * 3, 'GBD')
elif (oper_out == 'DungeonCom') and (oper_friend == 'AbobaMobile'):
    print(time * 2.25, 'GBD')
else:
    print('Choose correct operator, please! In the Republic of GachiBoba there are only two operators: Aboba Mobile and DungeonCom!')

# task 4
sell1 = int(input('Enter the sum of the sell for 1st manager: '))
sell2 = int(input('Enter the sum of the sell level for 2nd manager: '))
sell3 = int(input('Enter the sum of the sell  level for 3rd manager: '))
print()

if sell1 < 500:
    sal1 = 200 + sell1 / 100 * 3
elif (sell1 >= 500) and (sell1 < 1000):
    sal1 = 200 + sell1 / 100 * 5
elif sell1 >= 1000:
    sal1 = 200 + sell1 / 100 * 8

if sell2 < 500:
    sal2 = 200 + sell2 / 100 * 3
elif (sell2 >= 500) and (sell2 < 1000):
    sal2 = 200 + sell2 / 100 * 5
elif sell2 >= 1000:
    sal2 = 200 + sell2 / 100 * 8

if sell3 < 500:
    sal3 = 200 + sell3 / 100 * 3
elif (sell3 >= 500) and (sell3 < 1000):
    sal3 = 200 + sell3 / 100 * 5
elif sell3 >= 1000:
    sal3 = 200 + sell3 / 100 * 8

if (sal1 > sal2) and (sal1 > sal3):
    sal1 += 200
    print('The best worker of this month is 1st manager!')
elif (sal2 > sal1) and (sal2 > sal3):
    sal2 += 200
    print('The best worker of this month is 2nd manager!')
elif (sal3 > sal2) and (sal3 > sal1):
    sal3 += 200
    print('The best worker of this month is 3rd manager!')

print()

print('1st manager\'s salary now is ', sal1, 'USD')
print('2nd manager\'s salary now is ', sal2, 'USD')
print('3rd manager\'s salary now is ', sal3, 'USD')