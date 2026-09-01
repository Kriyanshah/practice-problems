list1 = []
list2 = []
for i in range(5):
    num = int(input("Enter a number for list1: "))
    list1.append(num)
for i in range(5):
    num = int(input("Enter a number for list2: "))
    list2.append(num)
list3 = list1 + list2
print("Combined list:", list3)