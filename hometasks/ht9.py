#Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом.
#Палиндром — слово или текст, которое читается одинаково слева направо и справа налево. Например, кок; А роза
#упала на лапу Азора; доход; А буду я у дуба
phrase = input('Enter any phrase: ')
noSpaces = phrase.replace(' ', '')
if noSpaces == noSpaces[::-1]:
    print('The phrase is palindrome')
else:
    print('The phrase isn\'t palindrome')