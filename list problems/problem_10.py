list = []
for i in range(1, 11):
    num = int(input("Enter value: "))
    list.append(num)

list.sort()

print("ascending list:", list)

list.sort(reverse=True)
print("descending list:", list)

print("the length of the list is:", len(list))