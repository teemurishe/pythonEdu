#task 1
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
for i in range(num1, num2 + 1):
	if i % 7 == 0 and i != 0:
		print(i)

#task 2
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print('All the numbers between:')
for i in range(num1, num2 + 1):
	print(i)
print('All the numbers between back:')
for i in range(num2, num1 - 1, -1):
    print(i)
print('Dividiable at 7:')
for i in range(num1, num2 + 1):
	if i % 7 == 0 and i != 0:
		print(i)
print('Dividiable at 5:')
num5 = 0
for i in range(num1, num2 + 1):
	if i % 5 == 0 and i != 0:
		num5 += 1
print(num5)

#task 3
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
for i in range(num1, num2 + 1):
	if (i % 3 != 0) and (i % 5 != 0):
		print(i)
	elif (i % 3 == 0) and (i % 5 == 0):
		print('Fizz Buzz')
	elif (i % 3 == 0) and (i % 5 != 0):
		print('Fizz')
	elif (i % 3 != 0) and (i % 5 == 0):
		print('Buzz')
	
	