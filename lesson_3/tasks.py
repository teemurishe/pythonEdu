 #task 1
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = 0

print((num1 + num2) / 2)
print()
for i in range(num1, num2 + 1):
    num3 += i

print(num3)