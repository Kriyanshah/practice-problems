numbers = [10,20,10,30,20,20,10,40,30]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print("The frequency of elements : ", frequency)