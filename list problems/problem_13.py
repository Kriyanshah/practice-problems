abbreviation = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
number = int(input("Enter a number between 1 and 12: "))
if 1 <= number <= 12:
    print("The abbreviation for month", number, "is", abbreviation[number - 1])
else:
    print("Invalid input. Please enter a number between 1 and 12.")