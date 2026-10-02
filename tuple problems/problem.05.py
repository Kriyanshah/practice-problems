<<<<<<< HEAD
numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list = []
for tuple in numbers:
    new_tuple = tuple[:-1] + (100,)
    list.append(new_tuple)
print("Original list = ", numbers)
=======
numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list = []
for tuple in numbers:
    new_tuple = tuple[:-1] + (100,)
    list.append(new_tuple)
print("Original list = ", numbers)
>>>>>>> a07aa88e1f09a1154c3c6bb23cb5b36a56fa49fd
print("New list = ", list)