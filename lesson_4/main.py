str1 = 'Hello world!'
print(str1.endswith('d'))
print(str1.startswith('Hell')) #true
print(str1.startswith('hell')) #false, cause the first letter is lower
print(str1.lower().startswith('hell')) #resolving the problem

str2 = '228822'
str3 = 'Hello'
str4 = '\n\n\n\n\n\n\n\n\n\n\n'
str5 = 'ABOBA'
str6 = 'microabobik'

print(str2.isalnum()) #true if all syms are nums
print(str3.isalpha()) #true with words only (without spec. syms)
print(str2.isdigit()) #true with nums (digits) only
print(str6.islower()) #true with little syms only
print(str4.isspace()) #only empty symbols allowed (spaces, enters etc.)
print(str3.istitle()) #only words from big letter allowed
print(str5.isupper()) #only uppercase letters allowed