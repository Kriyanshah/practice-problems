<<<<<<< HEAD
numbers = [10,20,10,30,20,20,10,40,30]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
=======
numbers = [10,20,10,30,20,20,10,40,30]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
>>>>>>> a07aa88e1f09a1154c3c6bb23cb5b36a56fa49fd
print("The frequency of elements : ", frequency)