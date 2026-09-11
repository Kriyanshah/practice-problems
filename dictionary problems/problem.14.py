my_dict = {
    "Amit": 89,
    "kriyan": 98,
    "taksh": 8,
    "Abdul": 87,
    "alyssa": 69
}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item : item[1])) #For ascending
print("Dictionary sorted by values in ascending order: ", sorted_dict)
sorted_dict = dict(sorted(my_dict.items(), key=lambda item : item[1], reverse = True)) #For descending
print("Dictionary sorted by values in descending order: ", sorted_dict)