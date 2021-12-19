#task 1
x = int(input('Enter any number: '))
y = int(input('Enter one more number: '))
print(x ** y)

#task 2
numSame = 0
for i in range(100, 999):
    c1 = i / 100
    c2 = (i / 10) % 10
    c3 = i % 10
    if (c1 == c2) or (c1 == c3) or (c2 == c3):
        numSame += 1
print(numSame)