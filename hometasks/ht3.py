#task 1
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
for i in range(num1, num2 + 1):
	if i % 7 == 0 and i != 0:
		print(i)
	