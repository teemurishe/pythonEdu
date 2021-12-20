#task 1
while True:
    num = input('Enter any number: ')
    numLength = len(num)
    sumDigs = 0
    averDigs = 0
    sumZero = 0
    oper = input('Select operation (1 - Sum of digits, 2 - Average of digits, 3 - How many zeros in your number): ')
    if oper == '1':
        for i in num:
            sumDigs += int(i)
        print(sumDigs)
    elif oper == '2':
        averDigs = sumDigs / numLength
        print(averDigs)
    elif oper == '3':
        for i in num:
            if i == '0':
                sumZero += 1
        print(sumZero)
