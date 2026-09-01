nums = []
for i in range(0, 20):
    num = int(input("enter value: "))
    nums.append(num)

print("\nlist:", nums)

print("\n similar elements amd index value")

for i in range(0, 20):
    if nums.count(nums[i])>1:
        print("\nNo:", nums[i], "->", end="")
    for j in range(20):
        if nums[j] == nums[i]:
            print("\n",j, end="")

print("\nEven and odd:")
even = 0
odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

print("\npositive and negative:")
positive = 0
negative = 0
for num in nums:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print("Number of positive numbers:", positive)
print("Number of negative numbers:", negative)