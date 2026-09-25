
def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", Add(a, b))
elif choice == 2:
    print("Result:", Subtract(a, b))
elif choice == 3:
    print("Result:", Multiply(a, b))
elif choice == 4:
    print("Result:", Divide(a, b))
else:
    print("Invalid choice")