from random import randint as rint
#part 1

#task 1
age = 15
name = 'Timur'
temp = 36.6
truth = True
marks = [5, 4, 4]
pets = {'Felix', 'Beggy', 'Panda', 'Kitty', 'Beary', 'Zabivaka', 'Musies'}
lovely = {'Food': 'French fries', 'Drink': 'Coca-Cola', 'Film': 'Titanic'}

#task 2
age = int(input('Enter your age: '))
if age >= 18 and age < 65:
    print('You\'re adult!')
elif age < 18:
    print('You\'re young!')
elif age >= 65:
    print('You\'re old!')

#task 3
print('Your marks:')
for i in marks:
    print(i)

#task 4
command = str()
while command != 'stop':
    command = input()
    if command != 'stop':
        print('Don\'t stop me now!')

#task 5
print('That\'s what you love most of all:')
for i in lovely:
    print(i)

#part 2

#task 1
list_1 = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
list_2 = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
list_3 = list(list_1 + list_2)

#task 2
list_3.sort()

#task 3
num = int(input('Enter any number: '))
if num % 15 == 0:
    print('Divisible by 15')
elif num % 3 == 0:
    print('Divisible by 3')
else:
    print('Divisible by 1')

#task 4
set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
print(set_1.intersection(set_2))

#task 5
string = input('Enter anything: ')
if string == string[::-1]:
    print('Palindrome confirmed!')
else:
    print('It\'s just another word... I\'m so tired...')

#part 3

#task 1
def numList(num1, num2):
    list_ = []
    list_.append(num1)
    list_.append(num2)
    print(list_)
numList(5, 8)

#task 2
def randList():
    list_ = []
    len = rint(1, 100)
    for i in range(1, len):
        list_.append(rint(-100, 100))
    list_.sort()
    print(list_)
randList()