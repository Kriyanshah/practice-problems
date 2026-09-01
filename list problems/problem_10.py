nums = []
for i in range(10):
    num = int(input("Enter a number: "))
    nums.append(num)
nums.sort()
print("Sorted list:", nums)
nums.sort(reverse=True)
print("Sorted list in descending order:", nums)

print("length of the list:", len(nums))