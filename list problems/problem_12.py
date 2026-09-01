phrase = input("Enter a phrase: ")
words = phrase.split()
acronym = ""
for word in words:
    acronym = acronym + word[0].upper()
print("Acronym:", acronym)