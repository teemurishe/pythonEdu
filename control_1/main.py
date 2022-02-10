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