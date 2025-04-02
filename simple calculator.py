def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponentiation")
print("7. Floor Division")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", modulus(num1, num2))
elif choice == '6':
    print("Result:", exponentiation(num1, num2))
elif choice == '7':
    print("Result:", floor_division(num1, num2))
else:
    print("Invalid input")
