#task 1
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

for i in range(num1, num2):
    numIter = 0
    primeNums = ''
    for a in range(2, i // 2 + 1):
        if (i % a == 0):
            numIter += 1
    if (numIter <= 0):
        primeNums += str(i)
        print(primeNums)

#task 2
num1 = 1
num2 = 10
for i in range(num1, num2 + 1):
    multSheet = str(i) + ' * 1 = ' + str(i * 1) + '    ' + str(i) + ' * 2 = ' + str(i * 2) + '    ' + str(i) + ' * 3 = ' + str(i * 3) + '    ' + str(i) + ' * 4 = ' + str(i * 4) + '    ' + str(i) + ' * 5 = ' + str(i * 5) + '    ' + str(i) + ' * 6 = ' + str(i * 6) + '    ' + str(i) + ' * 7 = ' + str(i * 7) + '    ' + str(i) + ' * 8 = ' + str(i * 8) + '    ' + str(i) + ' * 9 = ' + str(i * 9) + '    ' + str(i) + ' * 10 = ' + str(i * 10)
    print(multSheet)
    if i != num2:
        print ('------------------------------------------------------------------------------------------------------------------------')

#task 3
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
for i in range(num1, num2 + 1):
    multSheet = str(i) + ' * 1 = ' + str(i * 1) + '    ' + str(i) + ' * 2 = ' + str(i * 2) + '    ' + str(i) + ' * 3 = ' + str(i * 3) + '    ' + str(i) + ' * 4 = ' + str(i * 4) + '    ' + str(i) + ' * 5 = ' + str(i * 5) + '    ' + str(i) + ' * 6 = ' + str(i * 6) + '    ' + str(i) + ' * 7 = ' + str(i * 7) + '    ' + str(i) + ' * 8 = ' + str(i * 8) + '    ' + str(i) + ' * 9 = ' + str(i * 9) + '    ' + str(i) + ' * 10 = ' + str(i * 10)
    print(multSheet)
    if i != num2:
        print ('------------------------------------------------------------------------------------------------------------------------')