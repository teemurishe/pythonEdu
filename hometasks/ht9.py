#task 1
phrase = input('Enter any phrase: ')
noSpaces = phrase.replace(' ', '')
if noSpaces == noSpaces[::-1]:
    print('The phrase is palindrome')
else:
    print('The phrase isn\'t palindrome')

#task 2
phrase = input('Enter any phrase: ')
keyWords = input('Enter keywords without\',\': ')
keyList = keyWords.lower().split()
phraseList = phrase.lower().split()
for i in range(len(phraseList)):
    for a in range(len(keyList)):
        if keyList[a] == phraseList[i]:
            phraseList[i] = phraseList[i].upper()

print(' '.join(phraseList))