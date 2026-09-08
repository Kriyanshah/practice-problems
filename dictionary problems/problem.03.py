my_dict = {
    101: "Amit",
    102: "Rahul",
    103: "Priya"
}
key = int(input("Enter the key to search : "))
if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("key does not exist in the dictionary")