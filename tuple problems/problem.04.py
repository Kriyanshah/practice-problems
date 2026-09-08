numbers = (10, 20, 30, 40, 50)
element = int(input("enter your element: "))
if element in numbers:
    print("index of the number is : ", numbers.index(element))
else:
    print("element not found")
    