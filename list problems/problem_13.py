<<<<<<< HEAD
abbreviation = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
number = int(input("Enter a number between 1 and 12: "))
if 1 <= number <= 12:
    print("The abbreviation for month", number, "is", abbreviation[number - 1])
else:
=======
abbreviation = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
number = int(input("Enter a number between 1 and 12: "))
if 1 <= number <= 12:
    print("The abbreviation for month", number, "is", abbreviation[number - 1])
else:
>>>>>>> a07aa88e1f09a1154c3c6bb23cb5b36a56fa49fd
    print("Invalid input. Please enter a number between 1 and 12.")