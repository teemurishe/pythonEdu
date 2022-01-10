list1 = [0, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6]
set1 = set()
for i in list1:
    set1.add(i)
list1 = []
for i in set1:
    list1.append(i)
print(list1)