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