import random as rand
# task 1
# print(eval(input('Enter your operation: '))) #AAAHAHAHAHHAHAHAHAHAHHA

#task 2
randList = []
for i in range(1, rand.randint(1, 100)):
    randList.append(rand.randint(-100, 100))
posNum = 0
negNum = 0
zeroNum = 0
for i in randList:
    if i > 0:
        posNum += 1
    elif i < 0:
        negNum += 1
    elif i == 0:
        zeroNum += 1
print(randList)
print('Positive numbers: ', posNum, '\n', 'Negative numbers: ', negNum, '\n', 'Zeros: ', zeroNum)