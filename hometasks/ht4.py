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

# #task 2
# num = int(input('Enter any number: '))
# degree = int(input('Enter degree (from 1 to 7): '))
# if (degree < 1) or (degree > 7):
#     print('Incorrect degree. Choose degree from 1 to 7')
# else:
#     if degree == 1:
#         print(num)
#     elif degree == 2:
#         print(num * num)
#     elif degree == 3:
#         print(num * num * num)
#     elif degree == 4:
#         print(num * num * num * num)
#     elif degree == 5:
#         print(num * num * num * num * num)
#     elif degree == 6:
#         print(num * num* num* num * num * num)
#     elif degree == 7:
#         print(num * num * num * num * num * num * num)

#task 3
#Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит
#стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
time = int(input('Enter please time of your talk (in minutes): ')) #didn't understand the task: enter cost, choose operators and print cost
#probably, time of dialogue was ment in first input
oper_out = input('Choose your operator (AbobaMobile, DungeonCom): ')
oper_friend = input('Choose your partner\'s operator (same chose): ')
if oper_out == oper_friend: #calls in one network has same tariffs
    print(time * 1.5, 'GBD') #GBD - GachiBoba Dollars
elif (oper_out == 'AbobaMobile') and (oper_friend == 'DungeonCom'):
    print(time * 3, 'GBD')
elif (oper_out == 'DungeonCom') and (oper_friend == 'AbobaMobile'):
    print(time * 2.25, 'GBD')
else:
    print('Choose correct operator, please! In the Republic of GachiBoba there are only two operators: Aboba Mobile and DungeonCom!')