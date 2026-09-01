list1=[]
list2=[]
for i in range(6):
    num = int(input("Enter value: "))
    list1.append(num)

for i in range(6):
    num = int(input("Enter value: "))
    list2.append(num)

print("List 1:", list1)
print("List 2:", list2)

merged_list = list1 + list2
print("Merged list:", merged_list)