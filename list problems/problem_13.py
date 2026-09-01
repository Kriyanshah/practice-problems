abbreviation = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
value = int(input("Enter a number between 1 and 12: "))
if 1 <= value <= 12:
    print("The abbreviation for month", value, "is:", abbreviation[value - 1])
else:
    print("Invalid input. Please enter a number between 1 and 12.")
    