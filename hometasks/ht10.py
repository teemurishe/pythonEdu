import random

list1 = []
list2 = []
listAll = []
listAllNoReps = []
listAllBoth = []
listAllUniq = []
listAllMinMax = []
lengthList = random.randint(5, 10)
 
for i in range(lengthList):
    elem1 = random.randint(1, 100)
    list1.append(elem1)
    elem2 = random.randint(1, 100)
    list2.append(elem2)
    if elem1 == elem2:
        listAllBoth.append(elem1, elem2)
        listAllNoReps.append(elem1)
    if elem1 != elem2:
        listAllUniq.append(elem1)
    if elem2 != elem1:
        listAllUniq.append(elem2)

listAll.append(list1)
listAll.append(list2)

if min(list1) < min(list2):
    listAllMinMax.append(min(list1))
elif min(list2) < min(list1):
    listAllMinMax.append(min(list2))
if max(list1) > max(list2):
    listAllMinMax.append(max(list1))
elif max(list2) > max(list1):
    listAllMinMax.append(min(list2))

print(list1)
print(list2)
print(listAll)
print(listAllNoReps)
print(listAllBoth)
print(listAllUniq)
print(listAllMinMax)