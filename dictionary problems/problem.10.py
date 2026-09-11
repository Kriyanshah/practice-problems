mydict =  {
    "marks1": 23,
    "marks2": 123,
    "marks3": 43,
    "marks4": 13,
    "marks5": 39
}
total = sum(mydict.values())
mean = total / len(mydict)
print("The mean of all values : ", mean)