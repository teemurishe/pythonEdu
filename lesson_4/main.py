str1 = 'Hello world!'
print(str1.endswith('d'))
print(str1.startswith('Hell')) #true
print(str1.startswith('hell')) #false, cause the first letter is lower
print(str1.lower().startswith('hell')) #resolving the problem
