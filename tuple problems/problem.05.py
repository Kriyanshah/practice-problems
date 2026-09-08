numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list = []
for tuple in numbers:
    new_tuple = tuple[:-1] + (100,)
    list.append(new_tuple)
print("Original list = ", numbers)
print("New list = ", list)