list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 9, 10]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)