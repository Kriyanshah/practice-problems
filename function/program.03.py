
def largest_of_three(a, b, c):
    list = [a,b,c]
    list.sort()
    print(list[2])
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("largest : ", end="")
largest_of_three(a,b,c)