# Задание 1

# Есть некоторый текст (для теста возьмите текст рыбу). СОЗДАТЬ ПЕРЕМЕННУЮ СОДЕРЖАЩУЮ ТЕКСТ
# Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# Результат вывести на экран.
fishText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. (1.10.32/1.10.33)'
print('Choose operation:')
print('1. All first letters are upper')
print('2. How many numbers are found in the text')
print('3. How many symbols are found in the text')
oper = int(input('Your choice: '))
if oper == 1:
    fishList = fishText.split()
    for i in range(len(fishList)):
        str(fishList[i].capitalize())
        print(fishList[i])
    fishText = ' '.join(fishList)
    print(fishText) #fuckin stupid shit of stupid shit

# Задание 2

# дан список [0,1,2,3,...99,100], пользователь вводит цифру.
# Необходимо посчитать сколько раз данная цифра присутствует в списке.
# Результат вывести на экран.

# Задание 3

# Создать список [0,1,2,3,4,...99,100]
# Необходимо посчитать сумму всех элементов и их среднеарифметическое.
# Результаты вывести на экран.

# Задание 4

# Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
# на экран.

# Задание 5

# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
# количества на экран.

# Задание 6

# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

# Задание 7

# Пользователь вводит с клавиатуры строку и слово для поиска. 
# Посчитайте сколько раз в строке встречается
# искомое слово. 
# Полученное число выведите на экран.