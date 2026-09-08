numbers = (10,20,30,40,50)
tuple = (numbers[-1],) + numbers[1:-1] + (numbers[0],)
print("Original tuple : ", numbers)
print("Modified tuple : ", tuple)
